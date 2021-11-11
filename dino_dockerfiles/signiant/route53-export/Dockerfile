FROM alpine:latest

# bash
RUN apk -Uuv add coreutils bash bash-doc bash-completion curl groff less python py-pip && \
  pip install awscli && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*

RUN mkdir -p /app

RUN curl -s -L https://github.com/barnybug/cli53/releases/download/0.8.8/cli53-linux-386 -o /app/cli53

WORKDIR /app
COPY app/* ./
RUN chmod a+x *

ENTRYPOINT ["./backup_r53.sh"]
CMD ['']
