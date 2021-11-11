FROM centos:centos7

STOPSIGNAL TERM

ENV http_proxy ${http_proxy}

COPY contrib/* /tmp/

RUN mv /tmp/proxy_centos.sh /etc/profile.d/ \
    && chmod +x /etc/profile.d/proxy_centos.sh && . /etc/profile \
    && yum install -y \
        iptables \
        procps \
        psmisc \
        squid \
        nc \
    && clear_proxy && mv /tmp/squid.conf /etc/squid/squid.conf && mv /tmp/squid /root/ && squid -z -F 


EXPOSE 3128

ENTRYPOINT ["/bin/bash", "/root/squid"]

