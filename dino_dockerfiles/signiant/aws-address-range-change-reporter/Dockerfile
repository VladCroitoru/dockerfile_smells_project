FROM alpine:latest

# bash
RUN apk -Uuv add coreutils bash bash-doc bash-completion curl groff less python py-pip jq && \
  pip install awscli && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*

RUN mkdir -p /app

WORKDIR /app
COPY app/* ./
RUN chmod a+x *

ENTRYPOINT ["./aws-address-range-check.sh"]
CMD ['']
