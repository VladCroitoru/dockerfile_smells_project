FROM nginx:1.13-alpine

ARG ECS_GEN_RELEASE=0.4.0-custom

RUN apk add --update bash ca-certificates openssl \
    python py-setuptools py-pip && \
    pip install --upgrade pip && \
    pip install supervisor==3.3.3 && \
    rm -rf /var/cache/apk/* && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    sed -i 's/^http {/&\n    keepalive_requests 10000;/g' /etc/nginx/nginx.conf && \
    sed -i 's/worker_processes  1/worker_processes  auto/' /etc/nginx/nginx.conf && \
    sed -i 's/keepalive_timeout  65/keepalive_timeout  650/' /etc/nginx/nginx.conf && \
    wget -q https://github.com/madhu1512/ecs-gen/releases/download/$ECS_GEN_RELEASE/ecs-gen-linux-amd64.zip && \
    unzip ecs-gen-linux-amd64.zip && \
    cp ecs-gen-linux-amd64 /usr/local/bin/ecs-gen && \
    rm -rf ecs-gen-linux-amd64*

COPY nginx.tmpl nginx.tmpl
COPY supervisord.conf /etc/supervisor/
ENTRYPOINT ["supervisord", "--configuration", "/etc/supervisor/supervisord.conf"]
