FROM ubuntu:xenial
MAINTAINER juntaki<me@juntaki.com>

COPY env.sh /env.sh
COPY root.sh /root.sh
COPY setting.sh /setting.sh
COPY user.sh /user.sh
COPY setup.sh /setup.sh

RUN /setup.sh && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \
    rm /env.sh && \
    rm /root.sh && \
    rm /setting.sh && \
    rm /user.sh && \
    rm /setup.sh

EXPOSE 22
CMD    ["/usr/sbin/sshd", "-D"]