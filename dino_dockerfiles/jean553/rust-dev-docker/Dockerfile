# vim:set ft=dockerfile
FROM phusion/baseimage:master

# Only installs ansible's minimal required dependencies.

ENV SUDOFILE /etc/sudoers

COPY change_user_uid.sh /

RUN apt-get update -y && \
    apt-get upgrade -y

RUN apt-get install -y \
    python3-dev \
    python3-pip  \
    libffi-dev \
    libssl-dev \
    sudo

RUN pip3 install --upgrade \
    ansible \
    setuptools \
    packaging \
    pyparsing \
    appdirs

# ssh configuration for Vagrant usage
RUN \
    rm -f /etc/service/sshd/down && \
    echo 'PermitEmptyPasswords yes' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    useradd \
        --shell /bin/bash \
        --create-home --base-dir /home \
        --user-group \
        --groups sudo,ssh \
        --password '' \
        vagrant && \
    mkdir -p /home/vagrant/.ssh && \
    chown -R vagrant:vagrant /home/vagrant/.ssh && \
    chmod u+w ${SUDOFILE} && \
    echo '%sudo   ALL=(ALL:ALL) NOPASSWD: ALL' >> ${SUDOFILE} && \
    chmod u-w ${SUDOFILE}

COPY provisioning/ provisioning

# Execute ansible playbook(s).

RUN ansible-playbook provisioning/site.yml -c local

RUN chmod +x /change_user_uid.sh

ENTRYPOINT /change_user_uid.sh
CMD ["/sbin/my_init"]
