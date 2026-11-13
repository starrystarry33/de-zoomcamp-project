variable "project" {
  description = "GCP project ID"
  type        = string
  default     = "ny-rides-zoom"
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-west1"
}

variable "credentials" {
  description = "Path to the service account key file"
  type        = string
  default     = "gcp-key.json"
}

variable "gcs_bucket" {
  description = "GCS bucket name (must be globally unique)"
  type        = string
  default     = "ny-rides-zoom-taxi-data-z1xy"
}

variable "bq_dataset" {
  description = "BigQuery dataset ID"
  type        = string
  default     = "taxi_dataset"
}
