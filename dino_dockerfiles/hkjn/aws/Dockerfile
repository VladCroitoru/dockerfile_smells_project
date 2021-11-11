#
# Tools for interacting with Amazon Web Services.
#
# Specify credentials for the IAM user at run-time:
# $ docker run -e AWS_ACCESS_KEY_ID=foo \
#              -e AWS_SECRET_ACCESS_KEY=bar \
#              -e AWS_DEFAULT_REGION=eu-west-1 \
#              [this image] \
#              aws ec2 describe-instances
FROM hkjn/alpine

MAINTAINER Henrik Jonsson <me@hkjn.me>

# Install AWS CLI tools.
RUN apk --no-cache add python3 && \
    pip3 install --upgrade pip setuptools && \
    pip3 install awscli && \
    adduser -D awsuser

USER awsuser
WORKDIR /home/awsuser

ENTRYPOINT ["aws"]
