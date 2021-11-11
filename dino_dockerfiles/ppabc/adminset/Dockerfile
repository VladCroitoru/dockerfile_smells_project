FROM centos:7
MAINTAINER ppabc <ppabc@qq.com>

ENV TZ "Asia/Shanghai"
COPY adminset /opt/
RUN  bash /opt/install/server/auto_install.sh
ENTRYPOINT ["/usr/sbin/init"]
CMD ["/opt/start.sh"]
