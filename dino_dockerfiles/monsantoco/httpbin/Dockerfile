FROM gliderlabs/alpine:3.1

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install gunicorn httpbin \
  && echo '#!/bin/sh' > run.sh \
  && echo 'gunicorn --bind=0.0.0.0:80 httpbin:app' >> run.sh \
  && chmod +x run.sh \
  && rm -rf /var/cache/apk/* \
  && apk del python-dev \
     build-base

EXPOSE 80

CMD ["./run.sh"]
