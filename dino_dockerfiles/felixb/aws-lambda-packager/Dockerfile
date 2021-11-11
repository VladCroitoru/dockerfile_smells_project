FROM python:alpine

ENV \
    LAMBDA_NAME=lambda
WORKDIR /workdir
ENTRYPOINT ["/usr/local/bin/package.sh"]

RUN apk add --no-cache zip
RUN pip install virtualenv

COPY package.sh /usr/local/bin/
