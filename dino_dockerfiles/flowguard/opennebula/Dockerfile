FROM ubuntu:focal
ENV container docker

RUN DEBIAN_FRONTEND=noninteractive \
    ln -fs /usr/share/zoneinfo/Europe/Prague /etc/localtime && \
    apt-get update && \
    apt-get install -y curl wget openssh-server openssh-client lsb-release python3-pip ceph-common && \
    wget -q -O- https://downloads.opennebula.org/repo/Debian/repo.key | apt-key add - && \
    echo "deb https://downloads.opennebula.io/repo/6.0/Ubuntu/20.04 stable opennebula" > /etc/apt/sources.list.d/opennebula.list && \
    apt-get update && \
    apt-get install -y opennebula opennebula-sunstone opennebula-gate opennebula-flow opennebula-provision && \
    pip install envtpl && \
    apt-get clean

COPY start.sh start-as-oneadmin.sh /
COPY oned.conf.tpl /etc/one/
COPY vmm_exec_kvm.conf /etc/one/vmm_exec/

RUN echo > /etc/one/oned.conf && \
    chown oneadmin:oneadmin /etc/one/oned.conf /etc/one/oned.conf.tpl && \
    mv /var/lib/one /var/lib/one.orig && \
    rm /var/lib/one.orig/.one/* && \
    chown -R oneadmin /etc/ssh && \
    mkdir -p /var/run/sshd && \
    mv /etc/one/sunstone-views /etc/sunstone-views 

EXPOSE 2222 2633 4124 9869 29876

VOLUME /var/lib/one
VOLUME /etc/one

CMD /start.sh
