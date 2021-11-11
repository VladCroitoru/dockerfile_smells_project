FROM alpine:3.5

RUN apk add --update openssh \
 && rm -rf /var/cache/apk/* \
 && mkdir /var/run/sshd \
 && ssh-keygen -A \
 && passwd -d root \
 && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
 && sed -i 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/' /etc/ssh/sshd_config

CMD ["/usr/sbin/sshd", "-D"]
