FROM alpine:3.7

ENV CONSUL_TEMPLATES_VERSION=0.19.4 \
    CONSUL_TEMPLATES_SHA256=5f70a7fb626ea8c332487c491924e0a2d594637de709e5b430ecffc83088abc0

RUN apk add --virtual .buildpkgs --no-cache curl && \
    curl --fail --silent --show-error https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATES_VERSION}/consul-template_${CONSUL_TEMPLATES_VERSION}_linux_amd64.zip -o /tmp/consul-templates.zip && \
    apk del .buildpkgs && \
    echo "${CONSUL_TEMPLATES_SHA256}  /tmp/consul-templates.zip" > /tmp/consul-templates.sha256 && \
    sha256sum -c /tmp/consul-templates.sha256 && \
    cd /bin &&  \
    unzip /tmp/consul-templates.zip && \
    chmod +x /bin/consul-template && \
    rm /tmp/consul-templates.zip && \
    apk add --no-cache nginx python && \
    chown -R nginx:www-data /var/lib/nginx

ADD img /

RUN chmod +x /app/start.sh && \
    chmod +x /app/reload.sh && \
    chmod +x /app/generate.py

# Mount for certificates, they should be named private.pem and public.pem
VOLUME /security

EXPOSE 80 443

ENTRYPOINT ["/app/start.sh"]