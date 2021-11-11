FROM python:3.6.0-alpine

LABEL maintainer="Marvin Steadfast <marvin@xsteadfastx.org>" \
      description="A script to search for duplicates in Mayan EDMS and delete them through their API."

ENV DOCUMENT_PATH=/var/lib/mayan

COPY . /tmp/mayan-deduplicate/

RUN set -ex \
 && pip install /tmp/mayan-deduplicate/ \
 && rm -rf /tmp/mayan-deduplicate

ENTRYPOINT ["mayan-deduplicate"]
