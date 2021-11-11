FROM meteorhacks/mup-frontend-server
RUN ["sed", "-i", "--", "s/client_max_body_size 10M/client_max_body_size 200M/g", "/opt/nginx/conf/nginx.conf"]
