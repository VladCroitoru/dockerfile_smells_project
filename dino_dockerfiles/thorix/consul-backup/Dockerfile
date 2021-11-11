FROM alpine:latest
# Backup HashiCorp's Consul to AWS S3
# This will run the consul agent and then backup a consul snapshot every 30mins to S3

ENV CONSUL_VERSION 0.9.2
ENV CONSUL_SHA256 0a2921fc7ca7e4702ef659996476310879e50aeeecb5a205adfdbe7bd8524013

# Create a consul user and group first so the IDs get set the same way,
RUN addgroup consul && \
adduser -S -G consul consul

# Get Consul and AWS-cli
RUN apk --no-cache add curl ca-certificates python py-pip su-exec \
    && update-ca-certificates \
    && pip install awscli \
    && curl -sSL https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip -o /tmp/consul.zip \
    && echo "${CONSUL_SHA256}  /tmp/consul.zip" > /tmp/consul.sha256 \
    && sha256sum -c /tmp/consul.sha256 \
    && cd /bin \
    && unzip /tmp/consul.zip \
    && chmod +x /bin/consul \
    && rm /tmp/consul.zip \
    && apk --purge -v del py-pip

# Get Dumb-Init
RUN curl -sSL -o /usr//bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 \
    && chmod +x /usr//bin/dumb-init

COPY include/init.sh /

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/init.sh"]

