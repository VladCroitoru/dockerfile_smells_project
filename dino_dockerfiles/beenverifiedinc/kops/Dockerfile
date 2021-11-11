FROM alpine:3.5
RUN apk --no-cache update && \
    apk --no-cache add curl ca-certificates && \
    rm -rf /var/cache/apk/*
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/v1.10.7/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl
RUN curl -L https://github.com/kubernetes/kops/releases/download/1.10.0/kops-linux-amd64 -o /usr/local/bin/kops \
    && chmod +x /usr/local/bin/kops
ENTRYPOINT ["/usr/local/bin/kops"]
