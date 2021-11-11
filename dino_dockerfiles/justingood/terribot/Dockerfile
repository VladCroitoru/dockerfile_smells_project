FROM python:3.5-alpine

RUN apk --no-cache add ca-certificates curl && \
    curl -L "https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64" -o /bin/dumb-init && \
    chmod +x /bin/dumb-init && \
    apk del curl

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

RUN adduser -D -H terribot && \
    chown terribot: /app -R

USER terribot

ENTRYPOINT ["/bin/dumb-init", "--"]
CMD ["python", "terribot.py"]
