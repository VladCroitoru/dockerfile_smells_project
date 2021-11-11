FROM ubuntu:14.04
MAINTAINER BearD01001 <dino@beard.ink>

# Install packages
RUN apt-get -y update && \
    apt-get -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server ca-certificates pwgen supervisor git tar vim-nox vim-syntax-go wget curl --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install NodeJS@7.x
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - && \
    sudo apt-get install nodejs -y

# Install Koa and build web server
RUN mkdir -p /home/web/www /home/web/api /home/web/conf && \
    cd /home/web && \
    npm i koa && \
    npm i http-server -g

WORKDIR /home/web/www

RUN echo "<hr/><h1>Hello world!</h1><br/><h2>    -- BearD01001</h2><hr/>" > index.html

ADD http_server.conf /etc/supervisor/conf.d/

# Install MariaDB
RUN apt-get install -y software-properties-common && \
    apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db && \
    add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mariadb.nethub.com.hk/repo/10.1/ubuntu trusty main' && \
    apt-get -y update && \
    apt-get install -y --no-install-recommends mariadb-server && \
    apt-get clean all

# https://github.com/docker/docker/issues/6103
RUN mkdir -p /var/run/sshd && \
    sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
    sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config

# define volume
VOLUME /data/persistent

# Define working directory.
WORKDIR /data

ADD set_db_pw.sh /data/
ADD set_root_pw.sh /data/

ADD run.sh /data/

# As suggested here : http://docs.docker.com/articles/using_supervisord/
ADD supervisord.conf /etc/supervisor/conf.d/

ADD sshd.conf /etc/supervisor/conf.d/
ADD mysql.conf /etc/supervisor/conf.d/

RUN chmod a+x *.sh

# ## Strangely... docker.io don't want build this image since xterm env..
# # ENV TERM="xterm-color"

EXPOSE 22
CMD ["/data/run.sh"]
