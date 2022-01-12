"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

# # Create an AWS resource (S3 Bucket)
# bucket = s3.Bucket('my-bucket')
#
# # Export the name of the bucket
# pulumi.export('bucket_name', bucket.id)

# Create Health AWS Lambda
iam_for_health_lambda=aws.iam.Role(
    "iamHealthLambda",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts.AssumeRole",
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

health_lambda = aws.lambda_.Function(
    "healthLambda",
    code=pulumi.FileArchive(""),
    role=iam_for_health_lambda.arn,
    handler="app.lambda.handlers",
    runtime="python3.8",
    environment=aws.lambda_.FunctionEnvironmentArgs(
        variables={
            "foo": "bar"
        }
    )
)