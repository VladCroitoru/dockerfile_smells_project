FROM alpine:3.3

ADD start_runit /sbin/

RUN sed -i 's/#rc_sys=""/rc_sys="lxc"/g' /etc/rc.conf && \
    echo 'rc_provide="loopback net"' >> /etc/rc.conf && \
    sed -i 's/^#\(rc_logger="YES"\)$/\1/' /etc/rc.conf && \
    mkdir /etc/container_environment \
    && chmod a+x /sbin/start_runit && mkdir /etc/service && mkdir /etc/my_init.d && \
    echo "http://dl-4.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk --update upgrade && apk add runit curl python py-msgpack py-yaml py-jinja2 py-pip\
    py-requests py-zmq py-crypto py-m2crypto py-openssl libzmq py-cryptography py-cffi && \
    pip install tornado apache-libcloud docker-py url && rm -rf /var/cache/apk/*

ADD salt-minion.runit /etc/service/salt-minion/run
RUN chmod a+x /etc/service/salt-minion/run

RUN curl -o /tmp/salt-2015.8.1.tar.gz https://pypi.python.org/packages/source/s/salt/salt-2015.8.1.tar.gz && \
    tar -C /tmp -zxf /tmp/salt-2015.8.1.tar.gz && \
    cd /tmp/salt-2015.8.1 && python setup.py install
	
CMD ["/sbin/start_runit"]

