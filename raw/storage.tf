resource "aws_s3_bucket" "data_engineering_bucket" {    
    bucket = "${var.bucket_data_engineering_prefix}-${data.aws_caller_identity.current.account_id}-${var.user_name}"
    tags = local.common_tags
    
}

resource "aws_s3_bucket_acl" "bucket_acl" {  
  bucket = aws_s3_bucket.data_engineering_bucket.bucket
  acl    = "private"
}

resource "aws_s3_bucket_public_access_block" "public_access_block" {  
  bucket = aws_s3_bucket.data_engineering_bucket.bucket

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_ssm_parameter" "data_engineering_bucket_arn" {
  type  = "String"
  value = aws_s3_bucket.data_engineering_bucket.arn
  name = "bucket-name-${var.prefix}-project${var.environment}"
} 