FROM ubuntu:16.04
MAINTAINER dtgilles@t-online.de

##### install ssh without private keys
RUN    apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y ssh iptables \
    && apt-get clean \
    && find /var/lib/apt/lists -type f -exec rm -f {} \;

RUN    mkdir -p /var/run/sshd /etc/rose/ipin/.current /etc/rose/ipout/.current /var/opt/rose /etc/rose/bin/ \
    && sed s/101/0/ /usr/sbin/policy-rc.d \
    && rm -f /etc/ssh/*_key* /etc/update-motd.d/* \
    && :> /etc/motd

COPY sshd_config     /etc/ssh/sshd_config
COPY entry.sh        /entry.sh
COPY LoginSleep      add_user_keys.sh   init_ipout     /usr/local/bin/
COPY iptables.rose   iptables.conf      /etc/rose/bin/

ENV SSHD_OPTS	""
ENV LOGFILE	""

ENTRYPOINT ["/entry.sh"]
CMD ["sshd"]

EXPOSE 22
