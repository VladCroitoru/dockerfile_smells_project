FROM centos:6
#Installing and Enabling ssh

RUN yum -y install openssh-server openssh-clients sudo

# for some reason these steps seem necessary to enable connection
# To go through.
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd &&\
    mkdir -p /var/run/sshd
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN echo "        StrictHostKeyChecking no" >> /etc/ssh/ssh_config
# generate private and public keys
ADD ansible_id_rsa /root/.ssh/id_rsa
ADD ansible_id_rsa.pub /root/.ssh/id_rsa.pub
# allow future client with this public key to connect to this server
RUN cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/authorized_keys

RUN yum -y install tar wget unzip which

# Standard SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
