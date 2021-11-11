FROM centos:latest

RUN yum install -y \
    wget


RUN echo "Downloading torque rpms..." && \
    wget https://github.com/cbatchx/torquebuilder/releases/download/v4.2.10/torque-4.2.10-1.adaptive.el7.centos.x86_64.rpm -qO torque.rpm && \
    wget https://github.com/cbatchx/torquebuilder/releases/download/v4.2.10/torque-client-4.2.10-1.adaptive.el7.centos.x86_64.rpm -qO torque-client.rpm && \
    echo "Installing torque rpms..." && \
    rpm -i torque.rpm torque-client.rpm && \
    rm torque*.rpm

COPY ./config/config /var/spool/torque/mom_priv/
COPY entrypoint.sh /

EXPOSE 15002
EXPOSE 15003

ENTRYPOINT ["/entrypoint.sh"]
    
    