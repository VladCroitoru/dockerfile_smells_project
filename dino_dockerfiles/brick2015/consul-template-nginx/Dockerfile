FROM nginx:1.12-alpine

#Install Curl
RUN apk add --no-cache curl

#Download and Install Consul Template
ENV CT_URL https://releases.hashicorp.com/consul-template/0.18.2/consul-template_0.18.2_linux_amd64.tgz
RUN curl $CT_URL  | tar zx -C /usr/local/bin/
#Setup Consul Template Files
RUN mkdir /etc/consul-templates
RUN mkdir /etc/nginx/upstream
RUN echo "    include /etc/nginx/upstream/*.conf;" >> /etc/nginx/nginx.conf
RUN apk del curl
ENV CT_FILE /etc/consul-templates/nginx.conf

#Setup Nginx File
ENV NX_FILE /etc/nginx/upstream/app.conf

#Default Variables
ENV CONSUL consul:8500
ENV SERVICE consul-8500

# Command will
# 1. Write Consul Template File
# 2. Start Nginx
# 3. Start Consul Template

CMD echo -e "stream {                    \n\
  upstream app {                         \n\
  least_conn;                            \n\
  {{range service \"$SERVICE\"}}         \n\
  server  {{.Address}}:{{.Port}};        \n\
  {{else}}server 127.0.0.1:65535;{{end}} \n\
}                                        \n\
server {                                 \n\
  listen 8000;                           \n\
  proxy_pass app;                        \n\
  }                                      \n\
}" > $CT_FILE; \
/usr/sbin/nginx -c /etc/nginx/nginx.conf \
& CONSUL_TEMPLATE_LOG=debug consul-template \
  -consul=$CONSUL \
  -template "$CT_FILE:$NX_FILE:/usr/sbin/nginx -s reload";
