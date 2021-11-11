FROM ubuntu:16.04

RUN apt update -y && \
 apt install -y  emacs-nox zsh mlocate git sudo net-tools build-essential


COPY nginx_signing.key /root/nginx_signing.key
RUN apt-key add /root/nginx_signing.key

RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx\n deb-src http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >> /etc/apt/sources.list
RUN apt update -y
#RUN apt install -y unit
RUN apt install -y nginx
RUN apt install -y php-dev libphp-embed php7.0-mysql mysql-client

RUN git clone https://github.com/nginx/unit /tmp/unit && \
 cd /tmp/unit && \
 git checkout 8e2fd89634bedd4570a2d3d885c209a0e1d20d62 && \
 ./configure --prefix=/opt/unit && \
 ./configure php && \
 make && \
 make install

RUN apt install -y composer
# CMD ["/bin/bash"]
# CMD ["/usr/sbin/init"]
RUN service nginx start

CMD ["/opt/unit/sbin/unitd", "--no-daemon", "--control", "unix:/var/run/control.unit.sock"]


## 何もしないDockerにするときはこれ
# CMD ["sleep","3600"]

#ADD ./entrypoint.sh /usr/local/bin/entrypoint.sh
#RUN chmod a+x /usr/local/bin/entrypoint.sh
#CMD ['/usr/local/bin/entrypoint.sh']

# CMD ['/bin/bash']
# CMD ["/usr/local/unitd", "--no-daemon"]
# ENTRYPOINT ["/bin/bash"]
# VOLUME /var/run
# RUN sleep 3
# CMD socat UNIX-LISTEN:/var/run/control.unit.sock -
# CMD ["/usr/sbin/unitd", "--no-daemon"]
# RUN chmod 755 /var/run/control.unit.sock
# curl -X PUT -d @/root/json/start.json --unix-socket /run/control.unit.sock http://localhost/