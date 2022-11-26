variable "environment" {
  default = "dev"
}
variable "prefix" {
  default = "eBird"
}
variable "bucket_data_engineering_prefix" {
  default = "data-engineering"   
}
variable "user_name" {
  default = "gsantos"  
}
locals {
  prefix = var.prefix
  common_tags = {
    Environment = "${var.environment}"
    Project     = "${var.prefix}-${var.bucket_data_engineering_prefix}"
  }
}
variable "bucket_prefix_var" {
  description = "s3 bucket prefix"
  type        = list(string)
  default = [
    "raw",
    "cleaned",
    "curated",
    "consumed"
  ]
}
