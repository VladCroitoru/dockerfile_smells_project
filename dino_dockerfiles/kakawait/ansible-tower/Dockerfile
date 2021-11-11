# Ansible Tower Dockerfie
FROM ubuntu:xenial

LABEL maintainer thibaud.lepretre@gmail.com, mittell@gmail.com, reuben.stump@gmail.com, ybaltouski@gmail.com

ENV ANSIBLE_TOWER_VER 3.3.0-1

ENV PG_DATA /var/lib/postgresql/9.6/main

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

ADD http://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-${ANSIBLE_TOWER_VER}.tar.gz /opt/ansible-tower-setup-${ANSIBLE_TOWER_VER}.tar.gz

RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen "en_US.UTF-8" \
    && dpkg-reconfigure -f noninteractive locales \
    && apt-get install -y software-properties-common sudo apt-transport-https ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /var/log/tower \
    && tar xvf /opt/ansible-tower-setup-${ANSIBLE_TOWER_VER}.tar.gz -C /opt \
    && rm -f /opt/ansible-tower-setup-${ANSIBLE_TOWER_VER}.tar.gz

WORKDIR /opt/ansible-tower-setup-${ANSIBLE_TOWER_VER}
COPY inventory inventory

# Tower setup
RUN ./setup.sh -e "ansible_all_ipv6_addresses=[]" \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Docker entrypoint script
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# volumes and ports
VOLUME ["${PG_DATA}", "/certs"]
EXPOSE 443

CMD ["/docker-entrypoint.sh", "ansible-tower"]
