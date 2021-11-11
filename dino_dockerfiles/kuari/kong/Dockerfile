FROM kong:0.11
MAINTAINER kuari, kuari@justmylife.cc

RUN yum install git -y && \
    luarocks install kong-plugin-cookies-to-headers && \
    yum clean all

CMD ["/usr/local/openresty/nginx/sbin/nginx", "-c", "/usr/local/kong/nginx.conf", "-p", "/usr/local/kong/"]
