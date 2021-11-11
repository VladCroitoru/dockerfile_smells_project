FROM hypoport/ansible:2.4.2.0-1

RUN apk --no-cache add nodejs && \
  npm install -g serverless@1.26.0 && \
  pip install boto3 botocore


WORKDIR /ansible
