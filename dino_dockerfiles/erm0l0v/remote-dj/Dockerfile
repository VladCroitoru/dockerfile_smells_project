FROM node

# Keep upstart from complaining
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

RUN mkdir -p /var/log/nginx/ && \
    mkdir -p /remote_dj/api && \
    mkdir -p /remote_dj/dest && \
    apt-get update && \
    apt-get install -y libgeos-dev && \
    apt-get install -y nginx supervisor && \
    service supervisor stop && \
    service nginx stop

ADD ./config/supervisord.conf /etc/supervisord.conf
ADD ./config/nginx.conf /etc/nginx/nginx.conf

ADD package.json /remote_dj/package.json
ADD api/ /remote_dj/api/
ADD dest/ /remote_dj/dest/
WORKDIR /remote_dj

RUN npm install

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]

EXPOSE 80