import argparse
import logging
import sys
import pandas as pd
from sqlalchemy import create_engine
from time import time


def setup_logging(log_file="ingest.log"):
    # 同时往控制台和文件写日志，带时间戳和级别
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout),
        ],
    )


def main():
    parser = argparse.ArgumentParser(description="Download NYC taxi CSV and load into Postgres in chunks")
    parser.add_argument("--url", required=True, help="CSV file URL (.gz ok)")
    parser.add_argument("--table", required=True, help="Target table name")
    parser.add_argument("--chunksize", type=int, default=100000)
    parser.add_argument("--user", default="root")
    parser.add_argument("--password", default="root")
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", default="5432")
    parser.add_argument("--db", default="ny_taxi")
    parser.add_argument("--log-file", default="ingest.log")
    args = parser.parse_args()

    setup_logging(args.log_file)
    log = logging.getLogger(__name__)

    try:
        engine = create_engine(f"postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}")
        with engine.connect():
            pass  # 连不上立刻抛异常，不浪费时间下数据
        log.info("connected to postgres, loading into table: %s", args.table)

        df_iter = pd.read_csv(args.url, iterator=True, chunksize=args.chunksize, low_memory=False)
        first = True
        total = 0
        for i, df in enumerate(df_iter, start=1):
            t0 = time()
            for col in ("tpep_pickup_datetime", "tpep_dropoff_datetime"):
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col])
            df.to_sql(args.table, engine, if_exists="replace" if first else "append", index=False)
            total += len(df)
            log.info("chunk %d: %d rows in %.1fs (total %d)", i, len(df), time() - t0, total)
            first = False

        if total == 0:
            raise ValueError("no rows loaded - check the URL")
        log.info("DONE: %d rows -> %s", total, args.table)
        return 0  # 成功退出码
    except Exception:
        log.exception("ingest FAILED")  # 自动带 traceback 写进日志
        return 1  # 失败退出码


if __name__ == "__main__":
    sys.exit(main())  # 退出码透传给 shell，调度系统就靠这个判断成败
