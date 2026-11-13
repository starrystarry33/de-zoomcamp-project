output "gcs_bucket_name" {
  description = "Name of the created GCS bucket"
  value       = google_storage_bucket.taxi_bucket.name
}

output "bq_dataset_id" {
  description = "ID of the created BigQuery dataset"
  value       = google_bigquery_dataset.taxi_dataset.dataset_id
}
