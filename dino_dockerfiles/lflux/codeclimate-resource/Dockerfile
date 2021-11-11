FROM alpine

LABEL maintainer="ian.delahorne@gmail.com,svidrio@gmail.com"

RUN apk --no-cache add jq bash git curl

RUN curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > /usr/local/bin/cc-test-reporter
RUN chmod +x /usr/local/bin/cc-test-reporter

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*