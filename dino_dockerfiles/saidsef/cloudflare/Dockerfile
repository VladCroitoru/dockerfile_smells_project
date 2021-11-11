FROM python:2-alpine
MAINTAINER Said Sef <said@saidsef.co.uk> (http://saidsef.co.uk/)

LABEL version="2.0"
LABEL description="Containerised Cloudflare CLI"

ARG tkn=""
ARG email=""

ENV HOME /tmp
ENV tkn ${tkn:-''}
ENV email ${email:-''}

WORKDIR /opt/cloudflare

COPY . /opt/cloudflare

RUN apk --update add make autoconf
RUN pip install -r requirements.txt
RUN cd lib/ && pyflakes .
# Cleanup
RUN rm -rf /var/cache/apk/* && rm -rf ~/.cache/

ENTRYPOINT ["/opt/cloudflare/lib/cf_api.py"]
