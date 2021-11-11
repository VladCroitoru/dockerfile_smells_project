FROM debian:jessie-slim
LABEL maintainer="Michael Lynch <michael@mtlynch.io>"

ENV SIA_HOSTNAME="http://localhost"
ENV SIA_PORT 9980
ENV POLL_FREQUENCY 60
ENV OUTPUT_FILE metrics.csv

RUN apt-get update -y && \
    apt-get install -y git python2.7 python-pip python-dev

COPY . /sia-metrics-collector
WORKDIR /sia-metrics-collector

RUN pip install -r requirements.txt

# Clean up.
RUN rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/doc && \
    rm -rf /usr/share/man && \
    apt-get autoremove -y && \
    apt-get clean

ENTRYPOINT python sia_metrics_collector/main.py \
    --hostname "$SIA_HOSTNAME" \
    --port "$SIA_PORT" \
    --poll_frequency "$POLL_FREQUENCY" \
    --output_file "$OUTPUT_FILE"
