FROM ubuntu:14.04

WORKDIR /root

COPY scripts .

RUN chmod +x *.sh ;\
   ./upgrade_system.sh ;\
   ./setup_system.sh ;\
   ./get_senginx.sh ;\
   apt-get clean ;\
   echo "daemon off;" >> /usr/local/senginx/conf/nginx.conf

CMD ["/usr/local/senginx/sbin/nginx"]
