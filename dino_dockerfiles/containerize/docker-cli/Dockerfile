FROM docker:stable

RUN apk add --no-cache bash openssh openssh-client \
    && sed -i s/#PasswordAuthentication.*/PasswordAuthentication\ no/ /etc/ssh/sshd_config

COPY entrypoint.sh /usr/local/bin

COPY ssh /root/.ssh
RUN chmod 600 /root/.ssh/id_rsa && chmod 600 /root/.ssh/authorized_keys 
COPY ssh_config /etc/ssh/ssh_config

ENTRYPOINT ["entrypoint.sh"]
