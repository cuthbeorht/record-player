"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

# # Create an AWS resource (S3 Bucket)
# bucket = aws.s3.Bucket('my-bucket')
#
# # Export the name of the bucket
# pulumi.export('bucket_name', bucket.id)

# Create a RestAPI for the health path
todo_rest_api = aws.apigateway.RestApi(
    "TodoRestApi",
    description="This is the API Gateway used for the Todo app"
)
# Create a Resource to put in the API Gateway
todo_rest_resource = aws.apigateway.Resource(
    "healthResource",
    rest_api=todo_rest_api.id,
    parent_id=todo_rest_api.root_resource_id,
    path_part="health"
)

# Create a Method for the health path
todo_health_method = aws.apigateway.Method(
    "healthMethod",
    rest_api=todo_rest_api.id,
    resource_id=todo_rest_resource.id,
    http_method="GET",
    authorization="NONE"
)