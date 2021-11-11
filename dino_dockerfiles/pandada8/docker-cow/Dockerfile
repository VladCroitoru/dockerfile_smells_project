from alpine:latest

run apk add curl --no-cache -u gzip && \
    curl -L https://github.com/cyfdecyf/cow/releases/download/0.9.8/cow-linux64-0.9.8.gz > cow.gz && \
    gunzip cow.gz && chmod +x cow && \
    mkdir -p /app/.cow && mv cow /app && \
    curl -L https://raw.githubusercontent.com/cyfdecyf/cow/master/doc/sample-config/rc > /app/.cow/rc && \
    adduser -D -h /app cow && chown -R cow /app && apk del curl gzip

WORKDIR /app

USER cow

CMD ./cow --request=true

