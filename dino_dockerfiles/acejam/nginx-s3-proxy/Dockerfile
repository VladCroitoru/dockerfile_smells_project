FROM phusion/baseimage:0.9.19
MAINTAINER Joshua Noble <acejam@gmail.com>

RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

CMD ["/sbin/my_init"]

RUN add-apt-repository ppa:nginx/stable && \
    apt-get update && \
    apt-get install -y curl git build-essential && \
    cd /usr/src && \
    apt-get build-dep -y nginx && \
    apt-get source nginx

RUN cd /usr/src/nginx* && \
    git clone https://github.com/openresty/set-misc-nginx-module.git debian/modules/set-misc-nginx-module && \
    git clone https://github.com/simpl/ngx_devel_kit.git debian/modules/ngx_devel_kit && \
    git clone -b AuthV2 https://github.com/acejam/ngx_aws_auth.git debian/modules/ngx_aws_auth && \
    sed -i -e 's/--add-module=\$(MODULESDIR)\/nginx-development-kit \\/--add-module=\$(MODULESDIR)\/ngx_devel_kit \\\n \t\t\t--add-module=\$(MODULESDIR)\/set-misc-nginx-module \\\n \t\t\t--add-module=\$(MODULESDIR)\/ngx_aws_auth \\/g' debian/rules && \
    dpkg-buildpackage -us -uc && \
    dpkg -i ../nginx-common*.deb && \
    dpkg -i ../nginx-extras_*.deb

RUN mkdir -p /etc/service/nginx
ADD nginx.sh /etc/service/nginx/run
ADD default.conf /etc/nginx/sites-available/default
ADD nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
