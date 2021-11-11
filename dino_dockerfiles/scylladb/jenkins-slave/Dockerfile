FROM ubuntu:14.04
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install default-jre openssh-server sudo
RUN useradd -G sudo -d /jenkins -m jenkins
RUN echo 'jenkins ALL=(ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers
RUN mkdir /jenkins/.ssh
COPY authorized_keys /jenkins/.ssh/
RUN chown -R jenkins:jenkins /jenkins/.ssh
RUN chmod 700 /jenkins/.ssh
RUN chmod 600 /jenkins/.ssh/authorized_keys
RUN mkdir -p /var/run/sshd
RUN chmod 700 /var/run/sshd
EXPOSE 22
