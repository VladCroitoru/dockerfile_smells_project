FROM nginx:1.13

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list

RUN apt-get update && \
    apt-get install -y apache2-utils dnsmasq procps && \
    apt-get install -y certbot -t jessie-backports && \
    rm -r /var/lib/apt/lists/*

RUN echo "\n\n# Docker extra config \nuser=root\naddn-hosts=/etc/hosts\n" >> /etc/dnsmasq.conf

COPY nginx.conf /nginx.conf.template

COPY run.bash /run.bash

EXPOSE 80

CMD ["/bin/bash", "/run.bash"]

VOLUME /etc/letsencrypt
