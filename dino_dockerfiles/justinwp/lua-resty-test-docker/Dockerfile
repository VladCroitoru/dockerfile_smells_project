FROM openresty/openresty:1.11.2.2-xenial

# Install cpanm and Test::NGINX
RUN apt-get install -qq -y cpanminus && cpanm --notest Test::Nginx

RUN mkdir -p /opt/src
WORKDIR /opt/src

RUN apt-get update
RUN apt-get install expect apache2-utils libev4 libev-dev wget python -y
RUN wget http://cgit.lighttpd.net/weighttp.git/snapshot/weighttp-master.tar.gz && \
    tar xvf weighttp-master.tar.gz && cd weighttp-master && ./waf configure && ./waf build && ./waf install

RUN apt-get install expect -y

ENV PATH /usr/local/openresty/bin:/usr/local/openresty/luajit/bin/:$PATH
