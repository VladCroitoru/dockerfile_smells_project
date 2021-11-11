FROM python:2.7-alpine3.7

MAINTAINER pam79 <paapaabdullahm@gmail.com>

RUN pip install slack-cleaner

VOLUME ["/backup"]

WORKDIR /backup

ENTRYPOINT ["slack-cleaner"]
