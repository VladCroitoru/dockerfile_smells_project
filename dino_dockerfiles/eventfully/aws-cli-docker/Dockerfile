FROM amazonlinux:latest

RUN yum install -y aws-cli

ENV AWS_ACCESS_KEY_ID="dummyValue" AWS_SECRET_ACCESS_KEY="dummyValue"

ENTRYPOINT ["/usr/bin/aws"]
