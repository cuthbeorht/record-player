terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "pulumi-bot"
  region  = "us-east-1"
}

resource "aws_iam_role" "cloudwatch_role" {
  name = "cloudwatch_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "cloudwatch.amazonaws.com"
        }
      },
    ]
  })

  tags = {
    role_name = "cloudwatch_role"
  }
}

# Create an API Gateway
resource "aws_api_gateway_rest_api" "todo_rest_api" {
  name = "Todo Rest API"

  body = jsonencode({
    openapi = "3.0.1"
    info = {
      title   = "example"
      version = "1.0"
    }
    paths = {
      "/path1" = {
        get = {
          x-amazon-apigateway-integration = {
            httpMethod           = "GET"
            payloadFormatVersion = "1.0"
            type                 = "HTTP_PROXY"
            uri                  = "https://ip-ranges.amazonaws.com/ip-ranges.json"
          }
        }
      }
    }
  })

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}