FROM alpine:3.6

CMD ['kubectl']

RUN set -x                  && \
    apk --update upgrade    && \
    apk add ca-certificates && \
    rm -rf /var/cache/apk/*

ENV K8S_VERSION 1.22.2
RUN wget http://storage.googleapis.com/kubernetes-release/release/v${K8S_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl && \
    chmod 755 /usr/local/bin/kubectl

COPY kubectl_config.sh /kubectl_config.sh
RUN chmod +x /kubectl_config.sh

ENTRYPOINT ["/kubectl_config.sh"]
