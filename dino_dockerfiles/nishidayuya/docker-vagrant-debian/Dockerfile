FROM debian:8.9
MAINTAINER Yuya.Nishida. <yuya@j96.org>

RUN \
  set -x && \
  export DEBIAN_FRONTEND=noninteractive && \
  apt-get update && \
  apt-get install -y --no-install-recommends openssh-server sudo && \

  # "vagrant" User
  useradd -s /bin/bash vagrant && \
  echo vagrant:vagrant | chpasswd -m && \
  install -m 755 -o vagrant -g vagrant -d /home/vagrant && \
  install -m 700 -o vagrant -g vagrant -d /home/vagrant/.ssh && \
  echo 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key' > /home/vagrant/.ssh/authorized_keys \
  chmod 600 /home/vagrant/.ssh/authorized_keys && \
  chown vagrant:vagrant /home/vagrant/.ssh/authorized_keys && \

  # Root Password: "vagrant"
  echo root:vagrant | chpasswd -m && \

  # Password-less Sudo
  echo 'vagrant ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/vagrant && \

  # SSH Tweaks
  echo 'UseDNS no' >> /etc/ssh/sshd_config && \

  # Other Docker image fixes
  mkdir -p /var/run/sshd && \
  rm /usr/sbin/policy-rc.d && \

  # "vagrant-cachier" friendly
  rm /etc/apt/apt.conf.d/docker-clean && \

  # Cleanup
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
