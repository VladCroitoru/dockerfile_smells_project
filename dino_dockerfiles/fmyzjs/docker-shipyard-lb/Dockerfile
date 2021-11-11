from stackbrew/ubuntu:12.04
maintainer Shipyard Project "http://shipyard-project.com"
run apt-get update
run apt-get install -y libreadline-dev libncurses5-dev libpcre3-dev libssl-dev perl make wget
run wget http://openresty.org/download/ngx_openresty-1.4.3.3.tar.gz -O /tmp/nginx.tar.gz
run (cd /tmp && tar zxf nginx.tar.gz)
run (cd /tmp/ngx_* && ./configure --with-luajit)
run (cd /tmp/ngx_* && make install)
add run.sh /usr/local/bin/run
volume /var/log/shipyard
expose 80
expose 443
cmd ["/bin/sh", "-e", "/usr/local/bin/run"]
