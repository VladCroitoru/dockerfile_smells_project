FROM ubuntu:focal

ENV DEBIAN_FRONTEND noninteractive

# Add salt repo and install salt-ssh
ARG SALT_VERSION=__SALT_VERSION__
RUN apt-get update -y \
    && apt-get -qy install wget gnupg lsb-release \
    && echo "deb http://repo.saltstack.com/py3/ubuntu/$(lsb_release -sr)/amd64/${SALT_VERSION} $(lsb_release -sc) main" >> /etc/apt/sources.list.d/saltstack.list \
    && wget -qO - https://repo.saltstack.com/py3/ubuntu/$(lsb_release -sr)/amd64/${SALT_VERSION}/SALTSTACK-GPG-KEY.pub | apt-key add -
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends salt-ssh openssh-client

# Add utils
RUN apt-get install -y --no-install-recommends mc vim telnet iputils-ping curl ccze less jq

# Add sysadmws-utils for notify_devilry
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 2E7DCF8C && echo "deb https://repo.sysadm.ws/sysadmws-apt/ any main" >> /etc/apt/sources.list.d/sysadmws.list \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends sysadmws-utils-v1

# Copy notify_devilry.yaml from repo
COPY files/notify_devilry/__VENDOR__/notify_devilry.yaml /opt/sysadmws/notify_devilry/notify_devilry.yaml

# Cleanup
RUN rm -rf /var/lib/apt/lists/*

# Prepare SSH client
RUN mkdir -p -m 700 /root/.ssh
RUN echo "StrictHostKeyChecking no" > /etc/ssh/ssh_config.d/salt-ssh.conf

# Entrypoint with roster and salt-ssh key preparations and bash as default cmd
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash"]

# Fill the Salt in (this and next step should be in the end as they change layers each time)
RUN mkdir -p /srv
COPY files /srv/files
COPY formulas /srv/formulas
COPY pillar /srv/pillar
COPY salt /srv/salt
COPY salt_local /srv/salt_local
COPY scripts /srv/scripts
COPY README.md /srv/README.md
COPY etc/salt/roster* /etc/salt/
COPY etc/salt/master /etc/salt/master
COPY include /srv/include
COPY .salt-ssh-hooks /.salt-ssh-hooks

# Prepare pillar top.sls
WORKDIR /srv
RUN cat pillar/top_sls/_top.sls > pillar/top.sls && echo "" >> pillar/top.sls
RUN find pillar/top_sls \( \( -type f -o -type l \) -not -name _top.sls -a -not -name *.swp \) -print0 | sort -z | xargs -i -0 bash -c "cat {} >> pillar/top.sls; echo "" >> pillar/top.sls"
