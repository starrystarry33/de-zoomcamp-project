terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project     = var.project
  region      = var.region
  credentials = file(var.credentials)
}

resource "google_storage_bucket" "taxi_bucket" {
  name     = var.gcs_bucket
  location = var.region
}

resource "google_bigquery_dataset" "taxi_dataset" {
  dataset_id = var.bq_dataset
  location   = var.region
}
