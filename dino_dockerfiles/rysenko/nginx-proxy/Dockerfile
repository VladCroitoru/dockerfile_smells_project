FROM jwilder/nginx-proxy
ENV MAX_BODY_SIZE=50m
RUN { \ 
    sed -i 's/worker_connections\s*[0-9]*;/worker_connections 10000;/' /etc/nginx/nginx.conf; \
    sed -i 's/worker_processes\s*auto;/worker_processes 8; worker_rlimit_nofile 20000;/' /etc/nginx/nginx.conf; \
}
CMD { \
    echo "server_tokens off;"; \
    echo "client_max_body_size ${MAX_BODY_SIZE};"; \
} > /etc/nginx/conf.d/my_proxy.conf && forego start -r
