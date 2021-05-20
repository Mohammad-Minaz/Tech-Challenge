provider "aws" {
  region = var.region
}

resource "null_resource" "test-demo" {
  provisioner "local-exec" {
    command = "aws ec2 describe-instances --${var.option_type} ${var.option_value}"
  }
}