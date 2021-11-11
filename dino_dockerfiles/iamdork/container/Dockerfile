FROM centos:latest

RUN yum install epel-release -y
RUN yum install openssh-server supervisor -y

RUN mkdir -p /root/.ssh
ADD dork.pub /root/.ssh/authorized_keys
ADD generate_hostkey.sh /opt/generate_hostkey.sh
RUN chmod +x /opt/generate_hostkey.sh
ADD sshd.ini /etc/supervisord.d/sshd.ini
RUN echo "UseDNS no" >> /etc/ssh/sshd_config
RUN echo "AcceptEnv GIT_AUTHOR_EMAIL GIT_AUTHOR_NAME GIT_COMMITTER_NAME GIT_COMMITTER_EMAIL" >> /etc/ssh/sshd_config

EXPOSE 80

CMD ["/usr/bin/supervisord"]
