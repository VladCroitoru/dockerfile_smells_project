FROM gliderlabs/alpine:3.1
MAINTAINER Oliver Soell <oliver@soell.net>

RUN apk-install collectd collectd-curl collectd-rrdtool collectd-write_http py-pip btrfs-progs

RUN pip install envtpl
ADD collectd.conf.tpl /etc/collectd/collectd.conf.tpl
ADD collectd.d /etc/collectd/collectd.d
ADD btrfs-data.py /usr/local/bin/btrfs-data.py
CMD for template in /etc/collectd/collectd.conf.tpl /etc/collectd/collectd.d/*.tpl ; do envtpl $template ; done && exec collectd -f
