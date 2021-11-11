FROM johannessteu/docker-neos:latest
MAINTAINER Johannes Steu <js@johannessteu.de>

RUN apt-get update
RUN apt-get install -y git
RUN curl -L https://getcomposer.org/installer -o composer-setup.php && \
    php composer-setup.php && \
    rm  composer-setup.php && \
    mv composer.phar /usr/local/bin/composer && \
    chmod +rx /usr/local/bin/composer

RUN apt-get -y install openssh-server && \
    sed -i s/PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
    sed -i s/PermitEmptyPasswords.*/PermitEmptyPasswords\ yes/ /etc/ssh/sshd_config && \
    ssh-keygen -A

RUN mkdir /var/run/sshd

ADD /container-files/etc /etc