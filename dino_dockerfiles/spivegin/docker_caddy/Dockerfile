FROM bitnami/minideb:stretch

# ENV CADDY_VERSION 0.10.3 linux64 full
ENV CADDY_FEATURES "dns,hook.service,http.cgi,http.cors,http.expires,http.filemanager,http.filter,http.git,http.hugo,http.ipfilter,http.login,http.mailout,http.minify,http.proxyprotocol,http.ratelimit,http.realip,http.upload,net"
  #^ "cors,git,hugo,ipfilter,jsonp,search"
  # https://caddyserver.com/download/linux/amd64?plugins=dns,hook.service,http.cgi,http.cors,http.expires,http.filemanager,http.filter,http.git,http.hugo,http.ipfilter,http.login,http.mailout,http.minify,http.proxyprotocol,http.ratelimit,http.realip,http.upload,net
RUN install_packages tar git apt-transport-https ca-certificates
RUN mkdir /opt/caddy/ && mkdir /opt/caddy/tmp && mkdir /var/www/ && mkdir /opt/html
COPY ./files/caddy_v0.10.3_linux_amd64_custom_full.tar.gz /opt/caddy/tmp/
#COPY ./caddy_start.sh /opt/caddy/
# RUN chmod u+x /opt/caddy/caddy_start.sh
RUN  tar -xzf /opt/caddy/tmp/caddy_v0.10.3_linux_amd64_custom_full.tar.gz -C /opt/caddy/ && chmod u+x /opt/caddy/caddy
COPY ./files/Caddyfile /opt/caddy/
COPY ./files/index.html /opt/html
#RUN setcap 'cap_net_bind_service=+ep' /opt/caddy/caddy

EXPOSE 80 443
WORKDIR /opt/html

ENTRYPOINT ["/opt/caddy/caddy"]
CMD ["-agree=true","-email=ssl@txtsme.com", "-conf=/opt/caddy/Caddyfile", "-quiet=true", "-log=/var/log/caddy/server.log" ]

# ExecStart=/etc/caddy/caddy -agree=true -email=ssl@txtsme.com -pidfile=/run/caddy.pid -conf=/opt/caddy/Caddyfile -log=/var/log/caddy/server.log
