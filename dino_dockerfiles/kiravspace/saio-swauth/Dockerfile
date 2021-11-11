FROM kiravspace/saio-swauth:start-swift-supervisor
MAINTAINER kiravspace <kiravspace@gmail.com>

RUN git clone https://github.com/openstack/swauth.git -b 1.1.0 /root/swauth

WORKDIR /root/swauth
RUN python setup.py develop

ADD scripts/proxy-server.conf /etc/swift/proxy-server.conf
ADD scripts/proxy-server-noauth.conf /etc/swift/proxy-server-noauth.conf
ADD scripts/swift.conf /etc/swift/swift.conf
ADD scripts/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN /root/bin/remakerings && \
    swift-init main start && \
    sleep 3 && \
    swauth-prep -K swauthkey -A http://127.0.0.1:8081/auth/    

WORKDIR /root

CMD /root/bin/remakerings && \
    service supervisor start && \
    /bin/bash

EXPOSE 8018 8081

