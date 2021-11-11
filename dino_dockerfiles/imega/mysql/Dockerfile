FROM imega/base-builder:1.2.0

MAINTAINER Dmitry Gavriloff <info@imega.ru>

ADD build/rootfs.tar.gz /

EXPOSE 3306

VOLUME ["/data", "/etc/mysql/conf.d/"]

ENTRYPOINT ["mysqld"]

CMD ["--skip-grant-tables"]
