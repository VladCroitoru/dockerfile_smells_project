FROM php:7-alpine

LABEL maintainer="fabian.grassl@db-n.com"

ENV DEPLOYER_VERSION=5.1.3


RUN apk add --no-cache \
            bash \
            openssh-client \
            rsync

# Change default shell to bash (needed for conveniently adding an ssh key)
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

COPY ssh-deactivate-key-checking ssh-start-entrypoint ssh-add-known-host /bin/

COPY install_deployer.php /

RUN php /install_deployer.php
RUN rm /install_deployer.php

ENV LC_ALL=en_US.UTF-8

ENTRYPOINT ["ssh-start-entrypoint"]