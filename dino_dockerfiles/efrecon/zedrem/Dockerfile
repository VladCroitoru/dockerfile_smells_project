FROM debian:stretch-slim
MAINTAINER Emmanuel Frecon <efrecon@gmail.com>

ADD http://get.zedapp.org/zedrem-Linux-x86_64 /usr/local/bin/zedrem
RUN chmod a+x /usr/local/bin/zedrem

ENTRYPOINT ["/usr/local/bin/zedrem"]
