"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import datetime

health_api_gateway_log_group = aws.cloudwatch.LogGroup(
    "health_api_gateway_log_group",
    name="health_api"
)

# Create Health AWS Lambda
iam_for_health_lambda = aws.iam.Role(
    "iamHealthLambda",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Effect": "Allow",
                "Sid": ""             
            }
        ]
    }
    """
)

policy_for_health_lambda_logging = aws.iam.Policy(
    "health_api_gateway_lambda_loggin_policy",
    path="/",
    description="IAM policy for logging from a lambda",
    policy="""{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ],
          "Resource": "arn:aws:logs:*:*:*",
          "Effect": "Allow"
        }
      ]
    }
    """
)

## Attach logging policy to IAM Role
health_api_gateway_logging_policy_attachment = aws.iam.RolePolicyAttachment(
    "health_api_gateway_logging",
    role=iam_for_health_lambda.name,
    policy_arn=policy_for_health_lambda_logging.arn
)

health_lambda = aws.lambda_.Function(
    "healthLambda",
    code=pulumi.FileArchive("../../dist/lambda.zip"),
    role=iam_for_health_lambda.arn,
    handler="app.lambda.handler",
    runtime="python3.8",
    environment=aws.lambda_.FunctionEnvironmentArgs(
        variables={
            "foo": "bar"
        }
    )
)

health_api_gateway = aws.apigateway.RestApi(
    "health_apigateway"
)



health_api_gateway_resource = aws.apigateway.Resource(
    "health_api_gateway_resource",
    args=aws.apigateway.ResourceArgs(
        parent_id=health_api_gateway.root_resource_id,
        rest_api=health_api_gateway.id,
        path_part="{proxy+}"
    )
)

health_api_gateway_method = aws.apigateway.Method(
    "health_api_gateway_method",
    args=aws.apigateway.MethodArgs(
        authorization="NONE",
        http_method="ANY",
        resource_id=health_api_gateway_resource.id,
        rest_api=health_api_gateway.id
    )
)

health_api_gateway_deployment = aws.apigateway.Deployment(
    "health_deployment",
    rest_api=health_api_gateway.id,
    triggers={
        "date": str(datetime.datetime.now())
    },
    opts=pulumi.ResourceOptions(depends_on=health_api_gateway_method)
)

health_api_gateway_stage = aws.apigateway.Stage(
    "health_api_gateway_stage",
    deployment=health_api_gateway_deployment.id,
    rest_api=health_api_gateway.id,
    stage_name="test"
)

health_api_gateway_integration = aws.apigateway.Integration(
    "health_api_gateway_integration",
    args=aws.apigateway.IntegrationArgs(
        rest_api=health_api_gateway.id,
        resource_id=health_api_gateway_resource.id,
        http_method=health_api_gateway_method.http_method,
        type="AWS_PROXY",
        integration_http_method="POST",
        uri="arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:178062261621:function:healthLambda-27147a4/invocations"
    )
)