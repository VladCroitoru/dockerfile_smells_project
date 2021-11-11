FROM alpine:3.5
RUN apk --no-cache update && \
    apk --no-cache add ca-certificates curl && \
    rm -rf /var/cache/apk/*
RUN curl -L https://github.com/drone/drone-cli/releases/download/v0.8.0/drone_linux_amd64.tar.gz -o /usr/local/bin/drone.tar.gz \
    && tar -xvf /usr/local/bin/drone.tar.gz -C /usr/local/bin/ \
    && rm -rf /usr/local/bin/drone.tar.gz \
    && chmod +x /usr/local/bin/drone
ENTRYPOINT ["/usr/local/bin/drone"]
