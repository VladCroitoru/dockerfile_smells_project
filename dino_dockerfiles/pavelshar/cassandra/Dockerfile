FROM ubuntu:latest

RUN echo "root ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER root

ADD . /.docker
RUN chown -R root:root /.docker
RUN chmod -R 755 /.docker


# Build project
# Install and configure dependencies
RUN \
    sh /.docker/deploy/build/base.sh && \
    sh /.docker/deploy/build/ssh.sh


# Expose defaults 80 and 22 ports
EXPOSE 80 22


CMD \
    sh /.docker/deploy/init/entrypoint.sh && \
    sh /.docker/deploy/init/daemon.sh
