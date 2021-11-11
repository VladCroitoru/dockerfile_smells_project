From rabbitmq:3-management

ENV VERSION=3.6.12 \
    UVERSION=3_6_12

RUN \
    apt-get update && \
    apt-get install -y wget && \
    cd /usr/lib/rabbitmq/lib/rabbitmq_server-${VERSION}/plugins && \
    wget https://github.com/rabbitmq/rabbitmq-auth-backend-cache/releases/download/rabbitmq_v${UVERSION}/rabbitmq_auth_backend_cache-${VERSION}-otp-19.3.ez

