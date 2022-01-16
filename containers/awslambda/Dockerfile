FROM public.ecr.aws/lambda/python:3.8

COPY ./app ${LAMBDA_TASK_ROOT}

COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["app.lambda.handler"]