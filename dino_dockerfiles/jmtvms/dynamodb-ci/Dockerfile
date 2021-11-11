FROM jmtvms/dynamodb-local:stable

LABEL maintainer="joao@miguel.ms"
LABEL description="DynamoDB Container to be used with CI environments"
LABEL repository="https://github.com/jmtvms/dynamodb-ci.git"
LABEL bugs="https://github.com/jmtvms/dynamodb-ci/issues"
LABEL github="https://github.com/jmtvms/dynamodb-ci"
LABEL version="1.0.3"

#AWS access key.
ENV AWS_ACCESS_KEY_ID=
#AWS secret key.
ENV AWS_SECRET_ACCESS_KEY=
#AWS region.
ENV AWS_DEFAULT_REGION="us-east-1"
#output format (json, text, or table)
ENV OUTPUT="json"

# Installing AWS Cli
RUN apt-get update \
    && apt-get install -y python-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install awscli --upgrade


COPY extend.sh ./
RUN chmod +x extend.sh

ENTRYPOINT ["./extend.sh"]