FROM shurshun/alpine-moscow

LABEL author "Korviakov Andrey"
LABEL maintainer "4lifenet@gmail.com"

LABEL SERVICE_NAME="docker-health-bridge"

RUN \
    DOCKER_HB_VERSION=$(curl -s https://api.github.com/repos/shurshun/docker-health-bridge/tags | jq -r ".[0] .name") \
    && curl -fSlL https://github.com/shurshun/docker-health-bridge/releases/download/${DOCKER_HB_VERSION}/docker-health-bridge_${DOCKER_HB_VERSION}_linux_amd64.tar.gz | tar -C /bin -zx

ENTRYPOINT ["docker-health-bridge"]