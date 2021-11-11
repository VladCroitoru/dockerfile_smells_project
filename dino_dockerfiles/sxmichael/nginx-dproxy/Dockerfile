FROM nginx:1.9.4

RUN apt-get update && \
    apt-get install -y python && \
    rm -rf /var/lib/apt/lists/*

ENV APP /app
WORKDIR ${APP}
ADD . ${APP}

CMD ["/bin/bash", "start_nginx.sh"]
