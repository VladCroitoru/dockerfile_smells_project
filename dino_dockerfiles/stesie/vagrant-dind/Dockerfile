FROM jpetazzo/dind
MAINTAINER Stefan Siegl <stesie@brokenpipe.de>

# Basic upgrades; install sudo and SSH.
RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get install --no-install-recommends -y sudo openssh-server
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
RUN echo 'UseDNS no' >> /etc/ssh/sshd_config

# Remove the policy file once we're finished installing software.
# This allows invoke-rc.d and friends to work as expected.
RUN rm /usr/sbin/policy-rc.d

# Add the Vagrant user and necessary passwords.
RUN groupadd vagrant
RUN useradd -c "Vagrant" -g vagrant -G docker -d /home/vagrant -m -s /bin/bash vagrant
RUN echo 'root:vagrant' | chpasswd
RUN echo 'vagrant:vagrant' | chpasswd

# Allow the vagrant user to use sudo without a password.
RUN echo 'vagrant ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/vagrant

# Install Vagrant's insecure public key so provisioning and 'vagrant ssh' work.
RUN mkdir /home/vagrant/.ssh
ADD https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub /home/vagrant/.ssh/authorized_keys
RUN chmod 0600 /home/vagrant/.ssh/authorized_keys
RUN chown -R vagrant:vagrant /home/vagrant/.ssh
RUN chmod 0700 /home/vagrant/.ssh

EXPOSE 22
CMD ["/usr/local/bin/wrapdocker", "/usr/sbin/sshd", "-D"]

