FROM ubuntu:16.04
LABEL maintainer="Christian Ward-Garrison"

# Install dependencies.
# The final line upgrades all installed packages including kernel and kernel headers.
# "--force-confnew" means always install the new versions of configuration files.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python-software-properties \
       python-pip \
       software-properties-common \
       rsyslog \
       systemd \
       systemd-cron \
       sudo \
    && apt-get -yq dist-upgrade -o Dpkg::Options::="--force-confnew" \
    && rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

RUN sed -i 's/^\($ModLoad imklog\)/#\1/' /etc/rsyslog.conf
#ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf

# Upgrade pip. We'll use it to install Ansible later.
# Install the 'setuptools' package, which Ansible will need.
RUN pip install --upgrade pip setuptools

# Clearly initctl_faker systemd init within Docker, but I don't know anything more about it than that.
# Its origin is here: https://github.com/geerlingguy/drupal-vm/pull/456
COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl
