FROM centos:latest

RUN yum clean all && \
    yum -y install tree openssh-server

RUN useradd ansible && \
    mkdir /home/ansible/.ssh && \
    chown ansible:ansible /home/ansible/.ssh

ENV TZ=Asia/Singapore

## Suppress error message 'Could not load host key: ...'
RUN /usr/bin/ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -C '' -N ''
RUN /usr/bin/ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -C '' -N ''
RUN /usr/bin/ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -C '' -N ''
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
