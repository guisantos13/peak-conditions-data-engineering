data "aws_caller_identity" "current" {}

data "aws_ssm_parameter" "data_engineering_bucket_arn" {  
  name = "bucket-name-${var.prefix}-project${var.environment}"
} 