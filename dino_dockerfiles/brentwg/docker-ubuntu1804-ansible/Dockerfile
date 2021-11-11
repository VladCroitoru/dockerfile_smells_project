FROM ubuntu:18.04
LABEL maintainer="brentwg"

# Install dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python-software-properties \
       software-properties-common \
       rsyslog systemd systemd-cron sudo \
    && rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean
RUN sed -i 's/^\($ModLoad imklog\)/#\1/' /etc/rsyslog.conf
#ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf

# Install Ansible
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367 \
  && apt-add-repository "deb http://ppa.launchpad.net/ansible/ansible/ubuntu artful main" \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
     ansible \
  && rm -rf /var/lib/apt/lists/* \
  && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
  && apt-get clean

# Create brentwg user
RUN useradd -ms /bin/bash brentwg

COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

# Install Ansible inventory file
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts
