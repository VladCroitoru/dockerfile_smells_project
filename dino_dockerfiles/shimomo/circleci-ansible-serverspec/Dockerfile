FROM debian
MAINTAINER shimomo <yuichi@shimomo.net>

ENV DEBIAN_FRONTEND noninteractive

COPY sh/set_root_password.sh /set_root_password.sh
COPY sh/run.sh /run.sh

RUN chmod +x /*.sh \
    && apt-get clean \
    && apt-get update \
    && apt-get install -y openssh-server python sudo \
    && mkdir -p /var/run/sshd \
    && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
    && sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/" /etc/ssh/sshd_config \
    && useradd docker \
    && passwd -d docker \
    && mkdir /home/docker \
    && chown docker:docker /home/docker \
    && addgroup docker staff \
    && addgroup docker sudo \
    && echo "docker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/docker \
    && true

EXPOSE 22
CMD ["/run.sh"]
