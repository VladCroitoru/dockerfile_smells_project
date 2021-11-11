FROM python:3-alpine

LABEL maintainer="Said Sef said@saidsef.co.uk (saidsef.co.uk/)"

ARG BUILD_ID

ENV BUILD_ID ${BUILD_ID:-'beta-0'}
ENV VERSION "2.1"
ENV SLACK_API_TOKEN ${SLACK_API_TOKEN}
ENV SLACK_CHANNEL ${SKACK_CHANNEL}

WORKDIR /app

COPY spot.py /app
COPY requirements.txt /app

RUN apk add --update --no-cache ca-certificates && \
    pip --no-cache-dir install -r requirements.txt && \
    chown -R nobody .

USER nobody

CMD ["spot.py"]
ENTRYPOINT ["python"]
