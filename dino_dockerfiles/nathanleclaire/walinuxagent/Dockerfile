FROM debian:jessie

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gawk \
        rsyslog \
        openssl \
        ca-certificates \
        ssh \
        parted \
        sudo \
        net-tools \
        ifupdown \
        python \
        eject \
        python-pyasn1 \
        python-setuptools \
        python-rpm

COPY . /WALinuxAgent
WORKDIR /WALinuxAgent
RUN python setup.py install

# TODO: Migrate to alpine and/or do a slightly better job faking this to the
# agent.
RUN rm /etc/*version
RUN rm /etc/*release

COPY azurelinuxagent/distro/alpine/lsb-release /opt/lsb-release
COPY config/docker/waagent.conf /opt/waagent.conf
COPY bin/* /usr/sbin/
COPY /entrypoint.sh /entrypoint.sh

RUN chmod +x /usr/sbin/waagent && \
    ln -sf /dev/stdout /var/log/waagent.log

ENTRYPOINT ["/entrypoint.sh"]
