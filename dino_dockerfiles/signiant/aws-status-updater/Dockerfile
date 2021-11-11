FROM python:2.7-alpine

RUN apk -Uuv add coreutils bash bash-doc bash-completion curl groff less python py-pip ca-certificates && \
  pip install awscli && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*

RUN mkdir -p /app

WORKDIR /app
COPY app/* ./

RUN chmod a+x *
RUN pip install -r requirements.txt

ENTRYPOINT ["./update-aws-status-image.sh"]
CMD ['']
