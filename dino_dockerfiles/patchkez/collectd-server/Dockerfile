FROM ceph/base:tag-build-master-jewel-ubuntu-16.04

RUN apt-get update && \
    apt-get --no-install-recommends -y install collectd libpython2.7 python-pip git-core && apt-get clean && \
    pip install envtpl

ADD collectd_server.conf.tpl /etc/collectd/collectd.conf.tpl

ADD run.sh /root/run.sh

ENTRYPOINT ["/root/run.sh"]
