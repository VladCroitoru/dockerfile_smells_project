# Dockerfile for DevStack
# http://docs.openstack.org/developer/devstack/

FROM centos:7

MAINTAINER Tuan Vo <vohungtuan@gmail.com>


# Install yum tools
RUN set -x \
    && yum update -y \
    && yum install -y redhat-lsb-core epel-release iproute iptables python-pip git sudo \
    && yum groupinstall -y "Development Tools" --skip-broken \
    && yum clean all

# Set your Linux system hostname
# RUN set -x \
    # && hostnamectl set-hostname localhost

# Add Stack User
RUN set -x \
    && adduser stack \
    && echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
    && chown -R stack /opt

# Copy entrypoint file

COPY docker-entrypoint.sh /

RUN set -x \
 && chmod +x /docker-entrypoint.sh \
 && chown stack /docker-entrypoint.sh

USER stack

# Download DevStack
RUN set -x \
    && cd /opt \
    && mkdir -p /opt/stack/logs \
    && git clone https://git.openstack.org/openstack-dev/devstack

# Create a local.conf file
# with 4 passwords preset at the root of the devstack git repo.

COPY local.conf /opt/devstack/


# Customize the DevStack
RUN set -x \
    && cd /opt/devstack \
    && sed -ri 's@sudo sysctl@echo sudo sysctl@' tools/fixup_stuff.sh \
    && sed -ri 's@sudo sysctl@echo sudo sysctl@' lib/nova \
    && sed -ri 's@sudo \/bin\/systemctl restart \$1@sudo \/bin\/systemctl restart \$1 || true@' functions-common \
    && sed -ri 's@echo_summary "Starting RabbitMQ"@\t\techo_summary "Starting RabbitMQ"\n\t\tstart_service rabbitmq-server@' lib/rpc_backend
    
    # && sed -ri 's@restart_service openvswitch$@restart_service openvswitch || true@' lib/neutron_plugins/ovs_base \
    # && sed -ri 's@restart_service \$LIBVIRT_DAEMON@restart_service \$LIBVIRT_DAEMON || true@' lib/nova_plugins/functions-libvirt \
    # && sed -ri 's@restart_service rabbitmq-server@restart_service rabbitmq-server || true@' lib/rpc_backend \    



# Start the install
RUN set -x \
    && cd /opt/devstack \
    && ./stack.sh


EXPOSE 80
EXPOSE 5000
 
# Setup the ENV
# https://docs.docker.com/engine/reference/builder/#run

ENTRYPOINT ["/docker-entrypoint.sh"]

# CMD []

# Remove tmp
RUN find /opt/tmp/ -type f | xargs -L1 rm -f