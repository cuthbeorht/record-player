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


# Create Role for lambda
resource "aws_iam_role" "iam_for_todo_lambda" {
  name = "iam_for_todo_lambda"

  assume_role_policy = jsonencode(
    {
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Action" : "sts:AssumeRole",
          "Principal" : {
            "Service" : "lambda.amazonaws.com"
          },
          "Effect" : "Allow",
          "Sid" : ""
        }
      ]
  })
}

# Create AWS Lambda for Todo Rest API
resource "aws_lambda_function" "todo_lambda" {
  function_name = "todo_lambda"
  role          = aws_iam_role.iam_for_todo_lambda.arn
  handler       = "app.lambda.handler"
  runtime       = "python3.9"
  package_type  = "Image"
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

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

# Create an HTTP Resource ie. a URL path in API Gateway
resource "aws_api_gateway_resource" "proxy_resource" {
  parent_id   = aws_api_gateway_rest_api.todo_rest_api.root_resource_id
  path_part   = "{proxy+}"
  rest_api_id = aws_api_gateway_rest_api.todo_rest_api.id
}

# Create a Method to tie to the proxy
resource "aws_api_gateway_method" "proxy_method" {
  rest_api_id   = aws_api_gateway_rest_api.todo_rest_api.id
  resource_id   = aws_api_gateway_resource.proxy_resource.id
  http_method   = "ANY"
  authorization = "NONE"

  request_parameters = {
    "method.request.path.proxy" = true
  }
}

# Create an Integration with an AWS Lambda
#resource "aws_api_gateway_integration" "proxy_integration" {
#  http_method             = aws_api_gateway_method.proxy_method.http_method
#  resource_id             = aws_api_gateway_resource.proxy_resource.id
#  rest_api_id             = aws_api_gateway_rest_api.todo_rest_api.id
#  type                    = "AWS_PROXY"
#  integration_http_method = "POST"
#    uri = "uri of aws lambda - arn:aws:apigateway:${l}"
#}

resource "aws_api_gateway_deployment" "api_gateway_proxy_deployment" {
  depends_on = [
    aws_api_gateway_method.proxy_method,
    aws_api_gateway_resource.proxy_resource
  ]

  rest_api_id = aws_api_gateway_rest_api.todo_rest_api.id
  stage_name  = "dev"
  lifecycle {
    create_before_destroy = true
  }
}