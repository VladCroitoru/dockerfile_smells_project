FROM centos:centos6
MAINTAINER Benjamin Schwarze <benjamin.schwarze@mailboxd.de>

RUN yum update -y; yum clean all

RUN yum install -y openssh-server sudo tar wget; yum clean all

# generate SSH keys on first run
RUN /etc/init.d/sshd start

RUN sed -i 's/.*requiretty$/Defaults !requiretty/' /etc/sudoers

# SSH login fix to avoid user getting kicked off after login on some docker hosts
RUN sed -i -r 's/^session\s+required\s+pam_loginuid\.so/session optional pam_loginuid.so/g' /etc/pam.d/sshd

RUN groupadd vagrant && \
    useradd vagrant -g vagrant -G wheel && \
    echo "vagrant:vagrant" | chpasswd && \
    echo "vagrant   ALL=(ALL)   NOPASSWD: ALL" >> /etc/sudoers.d/vagrant && \
    chmod 0440 /etc/sudoers.d/vagrant

RUN mkdir -pm 700 /home/vagrant/.ssh && \
    wget --no-check-certificate 'https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub' -O /home/vagrant/.ssh/authorized_keys && \
    chmod 0600 /home/vagrant/.ssh/authorized_keys && \
    chown -R vagrant /home/vagrant/.ssh

# expose SSH port
EXPOSE 22

# run SSH daemon
CMD ["/usr/sbin/sshd", "-D"]
