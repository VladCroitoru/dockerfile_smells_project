FROM alpine:3.7
LABEL maintainer "mch1307@gmail.com"

# Set environment
ENV SERVICE_NAME=traefik \
    SERVICE_HOME=/opt/traefik \
    SERVICE_VERSION=v1.4.6 \
    SERVICE_URL=https://github.com/containous/traefik/releases/download
ENV SERVICE_RELEASE=${SERVICE_URL}/${SERVICE_VERSION}/traefik_linux-amd64 \
    PATH=${PATH}:${SERVICE_HOME}/bin

# Download and install traefik
RUN mkdir -p ${SERVICE_HOME}/bin ${SERVICE_HOME}/etc ${SERVICE_HOME}/log ${SERVICE_HOME}/certs ${SERVICE_HOME}/acme && \
    apk add --no-cache bash curl ca-certificates && \
    cd ${SERVICE_HOME}/bin && \
    curl -jksSL "${SERVICE_RELEASE}" -O && \
    mv traefik_linux-amd64 traefik && \
    touch ${SERVICE_HOME}/etc/rules.toml && \
    chmod +x ${SERVICE_HOME}/bin/traefik && \
    apk del curl
ADD opt /
RUN chmod +x ${SERVICE_HOME}/bin/*.sh && \
    chmod +x ${SERVICE_HOME}/bin/traefik
EXPOSE 8000
EXPOSE 80
EXPOSE 443

WORKDIR $SERVICE_HOME
ENTRYPOINT ["/opt/traefik/bin/traefik-service.sh","start"]
