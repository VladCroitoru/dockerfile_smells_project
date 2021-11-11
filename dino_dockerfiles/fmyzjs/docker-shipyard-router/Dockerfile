from stackbrew/ubuntu:12.04
maintainer Shipyard Project "http://shipyard-project.com"
run apt-get -qq update
run apt-get install -y g++ make python-dev python-setuptools libreadline-dev libncurses5-dev libpcre3-dev libssl-dev perl make wget git-core
run wget http://nodejs.org/dist/v0.8.26/node-v0.8.26.tar.gz -O /tmp/node.tar.gz
run (cd /tmp && tar zxf node.tar.gz)
run (cd /tmp/node-* && ./configure)
run (cd /tmp/node-* && make install)
run npm install -g hipache
add run.sh /usr/local/bin/run
volume /var/log/shipyard
expose 80
expose 443
cmd ["/bin/sh", "-e", "/usr/local/bin/run"]
