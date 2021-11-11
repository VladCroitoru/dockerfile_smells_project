FROM nginx:1.9

RUN sed -i 's/^http {/&\n    server_names_hash_bucket_size 128;/g' /etc/nginx/nginx.conf
RUN sed -i 's/^http {/&\n    client_max_body_size 200m;/g' /etc/nginx/nginx.conf

COPY proxy.conf /etc/nginx/proxy.conf
