FROM centos:latest

RUN yum install -y \
    wget


RUN echo "Downloading torque rpms..." && \
    wget https://github.com/cbatchx/torquebuilder/releases/download/v4.2.10/torque-4.2.10-1.adaptive.el7.centos.x86_64.rpm -qO torque.rpm && \
    wget https://github.com/cbatchx/torquebuilder/releases/download/v4.2.10/torque-server-4.2.10-1.adaptive.el7.centos.x86_64.rpm -qO torque-server.rpm && \
    echo "Installing torque rpms..." && \
    rpm -i torque.rpm torque-server.rpm && \
    rm torque*.rpm

# Create torque dirs
RUN mkdir -p /var/spool/torque/checkpoint/ && \
    mkdir -p /var/spool/torque/server_priv
    
COPY ./scripts/torque.setup /torque.setup

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]