FROM jfloff/alpine-python:2.7

RUN apk add --no-cache expect openssh openssh-sftp-server lftp rsync curl wget git sshpass

RUN ssh-keygen -A &&\
    ssh-keygen -t rsa -f ~/.ssh/id_rsa -N '' &&\
    cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys &&\
    chmod 600 ~/.ssh/authorized_keys &&\
    echo 'root:root' | chpasswd &&\
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D", "-e"]


