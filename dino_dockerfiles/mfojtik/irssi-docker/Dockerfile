FROM centos
MAINTAINER Michal Fojtik <mi@mifo.sk>
RUN yum install -y irssi openssh-server tmux && yum clean all

ENV IRC_USER irc
EXPOSE 2222
RUN useradd $IRC_USER && \
    mkdir -p /var/run/sshd && chown -R $IRC_USER /var/run/sshd /etc/ssh && \
    chmod 0777 /var/run && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

USER $IRC_USER
ADD sshd_config /etc/ssh/sshd_config
ADD run_sshd.sh /usr/local/bin/run_sshd.sh
CMD ["/usr/local/bin/run_sshd.sh"]
