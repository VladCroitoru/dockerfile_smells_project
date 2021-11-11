FROM debian

MAINTAINER MoeArt Developmemnt Team <dev@art.moe>

ENV NGINX_VERSION tengine-2.1.2_f
ENV OPENRESTY_VERSION openresty-1.11.2.1

ENV   DEBIAN_FRONTEND noninteractive
ENV   LANGUAGE en_US.UTF-8
ENV   LANG en_US.UTF-8
ENV   LC_ALL en_US.UTF-8

# Configure timezone and locale
RUN apt-get update && \
    apt-get install -y locales && \
    echo en_US.UTF-8 UTF-8 > /etc/locale.gen && \
    locale-gen && \
    dpkg-reconfigure locales

WORKDIR /usr/src/
ADD https://github.com/alibaba/tengine/archive/${NGINX_VERSION}.tar.gz tengine.tar.gz
ADD https://openresty.org/download/${OPENRESTY_VERSION}.tar.gz openresty.tar.gz
ADD https://github.com/xsec-lab/x-waf/archive/master.tar.gz x-waf.tar.gz
ADD https://github.com/xsec-lab/x-waf-admin/releases/download/x-waf-admin0.1/x-waf-admin0.1-linux-amd64.tar.gz x-waf-admin.tar.gz

RUN apt-get update && \
    apt-get -y install libreadline-dev \
                       libncurses5-dev \
                       libpcre3-dev \
                       libssl-dev \
                       perl \
                       openssl \
                       make \
                       build-essential && \
    tar -zxf openresty.tar.gz && \
    cd ${OPENRESTY_VERSION}/bundle/nginx-* && \
    rm -rf ./*  && \
    mv /usr/src/tengine.tar.gz . && \
    tar -zxf tengine.tar.gz && \
    cd tengine-${NGINX_VERSION} && \
    cp -R ./* ../ && \
    cd .. && \
    rm -rf tengine-${NGINX_VERSION}/ && \
    rm -rf tengine.tar.gz && \
    sed -i " \
        /#define TENGINE.*/s/\"Tengine/\"MoeArt Maid-chan/; \
        /#define tengine_version.*/s/[0-9]\{7\}/`date +%y%m0%d`/; \
        /#define TENGINE_VERSION.*/s/\".*\"/\"`date +%y.%m.%d`\"/; \
        /#define NGINX_VER.*/s/\"nginx/\"MoeArt Maid-chan/; \
        /#define NGINX_VAR.*/s/\"NGINX/\"MoeArt Maid-chan/; \
        " src/core/nginx.h && \
    sed -i " \
        s/ Sorry for the inconvenience./ And, Maid-chan donot know what you need./; \
        s/Please report this message and include the following information to us./Please report this message and include the following information to Maid-chan./; \
        s/Thank you very much/Inconvenience to you my sincere apologies/; \
        " src/http/ngx_http_special_response.c && \
    cd /usr/src/${OPENRESTY_VERSION} && \
    ./configure && \
    make -j4 && \
    make install && \
    cd /usr/local/openresty/nginx/conf/ && \
    mv /usr/src/x-waf.tar.gz . && \
    tar -zxf x-waf.tar.gz && \
    mv x-waf-master/ x-waf/ && \
    rm -rf x-waf.tar.gz && \
    ln -sf /dev/stdout /usr/local/openresty/nginx/logs/access.log && \
    ln -sf /dev/stderr /usr/local/openresty/nginx/logs/error.log && \
    cd /opt && \
    mv /usr/src/x-waf-admin.tar.gz . && \
    tar -zxf x-waf-admin.tar.gz && \
    rm -rf x-waf-admin.tar.gz && \
    apt-get -y remove build-essential && \
    dpkg --get-selections | awk '{print $1}'|cut -d: -f1|grep -- '-dev$' | xargs apt-get remove -y && \
    rm -rf /usr/src && \
    apt-get clean all && \
    rm -rf /tmp/* && \
    apt-get autoremove -y

ADD nginx.conf /usr/local/openresty/nginx/conf/nginx.conf
ADD xwaf /xwaf
ADD init.sql /tmp/init.sql
ADD init_sql.sh /tmp/init_sql.sh
RUN chmod +x /xwaf && \
    chmod +x /tmp/init_sql.sh && \
    /tmp/init_sql.sh && \
    mysql -u root -ppassword < /tmp/init.sql && \
    rm -rf /tmp/init.sql && \
    rm -rf /tmp/init_sql.sh

WORKDIR /opt/x-waf-admin
EXPOSE 80 443 5000
CMD ["/xwaf"]
