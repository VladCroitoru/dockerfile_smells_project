FROM python:3-alpine
LABEL maintainer "Mathias Söderberg <mths@sdrbrg.se>"

COPY requirements.txt /tmp/requirements.txt
COPY trannounce /usr/local/bin/trannounce

RUN pip install --no-cache-dir --requirement /tmp/requirements.txt && \
  rm -f /tmp/requirements.txt

ENTRYPOINT ["/usr/local/bin/trannounce"]
