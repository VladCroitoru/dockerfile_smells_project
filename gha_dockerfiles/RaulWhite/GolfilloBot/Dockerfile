ARG platform=library
FROM ${platform}/python:alpine

WORKDIR /app
COPY requirements.txt ./
RUN apk --no-cache add build-base libffi-dev openssl-dev jpeg-dev zlib-dev freetype-dev && \
    pip install -r requirements.txt && \
    rm /app/requirements.txt && \
    apk --no-cache del build-base libffi-dev openssl-dev && \
    apk --no-cache add libffi openssl
COPY golfillobot/ ./golfillobot

ENV PYTHONPATH=/app/
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

CMD python3 golfillobot/main.py