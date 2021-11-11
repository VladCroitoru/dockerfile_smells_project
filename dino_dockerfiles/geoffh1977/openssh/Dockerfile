# OpenSSH Docker Image - Ideal As A Quick Jumpbox
FROM alpine:3.7
MAINTAINER geoffh1977 <geoffh1977@gmail.com>

# Add Packages And Create Default Config Path
RUN  apk -U add openssh openssh-client bash && \
  rm -rf /var/cache/apk/* && \
  mkdir /etc/ssh-default;

# Load Default Config And Scripts
COPY assets/sshd_config /etc/ssh-default/sshd_config
COPY assets/start.sh /usr/local/bin/start.sh

RUN chmod 755 /usr/local/bin/start.sh && \
  rm -rf /etc/ssh && \
  mkdir -p /etc/ssh && \
  touch /var/log/btmp && \
  chmod 0600 /var/log/btmp && \
  touch /etc/motd

# Set Port
EXPOSE 22/tcp

# Start Command
ENTRYPOINT ["/usr/local/bin/start.sh"]
