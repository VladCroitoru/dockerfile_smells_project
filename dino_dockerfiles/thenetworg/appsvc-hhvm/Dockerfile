FROM hhvm/hhvm:latest
MAINTAINER Jan Hajek <hajek.j@hotmail.com>

COPY init_container.sh /bin/

ADD server.ini /etc/hhvm/server.ini
RUN touch /etc/hhvm/site.ini \
    && echo "root:Docker!" | chpasswd \
    && apt update \
    && apt install -y --no-install-recommends openssh-server \
    && chmod 755 /bin/init_container.sh 

COPY sshd_config /etc/ssh/

EXPOSE 2222 80

CMD ["/bin/init_container.sh"]
