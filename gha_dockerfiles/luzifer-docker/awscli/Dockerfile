FROM python:3-alpine

COPY requirements.txt /tmp/

RUN set -ex \
 && pip install --no-cache-dir -r /tmp/requirements.txt \
 && rm /tmp/requirements.txt \
 && apk --update add groff less

VOLUME ["/root/.aws"]

ENTRYPOINT ["/usr/local/bin/aws"]
CMD ["help"]
