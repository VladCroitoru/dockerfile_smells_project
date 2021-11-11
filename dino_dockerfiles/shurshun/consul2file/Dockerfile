FROM shurshun/alpine-moscow

LABEL author "Korviakov Andrey"
LABEL maintainer "4lifenet@gmail.com"

ENV CONSUL_ADDR=localhost:8500
ENV KEY_PREFIX=storage
ENV STORE_DIR=/tmp

RUN \
    CONSUL_VERSION=$(curl -s https://api.github.com/repos/hashicorp/consul/tags | jq -r ".[0] .name" | tr -d v) \
    && curl -fSl https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip -o /tmp/consul.zip \
    && unzip /tmp/consul.zip -d /bin \
    && rm -f /tmp/consul.zip

RUN \
    CONSUL2FILE_VERSION=$(curl -s https://api.github.com/repos/shurshun/consul2file/tags | jq -r ".[0] .name") \
    && curl -fSlL https://github.com/shurshun/consul2file/releases/download/${CONSUL2FILE_VERSION}/consul2file_${CONSUL2FILE_VERSION}_linux_amd64.tar.gz | tar -C /bin -zx

COPY bin/ /bin/

CMD ["entrypoint.sh"]
