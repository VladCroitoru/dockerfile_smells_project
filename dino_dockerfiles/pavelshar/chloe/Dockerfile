FROM node:alpine

RUN echo "root ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER root

ADD . /.docker
RUN chown -R root:root /.docker
RUN chmod -R 755 /.docker


# Install dependencies
RUN apk add --update \
    openssh \
    mc \
    git && \
    sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
    ssh-keygen -A

EXPOSE 80 22
CMD sh /.docker/deploy/entrypoint.sh && sh /.docker/deploy/daemon.sh
