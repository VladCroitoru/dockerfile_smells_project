FROM ubuntu:latest
MAINTAINER truthadjustr@gmail.com

RUN apt-get update && apt-get install -y --no-install-recommends\
    openssh-server\
    && rm -rf /var/lib/apt/lists/*\
    && useradd -ms /bin/bash guser\
    && mkdir /home/guser/.ssh\
    && chmod 700 /home/guser/.ssh

COPY sshd_config /etc/ssh/
COPY docker-entrypoint.sh /
COPY authorized_keys /home/guser/.ssh/
RUN chmod 600 /home/guser/.ssh/authorized_keys \
    && chown -R guser:guser /home/guser/.ssh/ \
    && echo "guser:password" | chpasswd \
    && mkdir /var/run/sshd \
    && chmod 0755 /var/run/sshd

EXPOSE 22

#CMD ["/usr/sbin/service","ssh","start"]
#CMD ["/usr/sbin/sshd","-p","22","-D","-d","-e"]
CMD ["/docker-entrypoint.sh"]
