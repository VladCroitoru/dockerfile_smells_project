
FROM million12/php-app-ssh:latest
MAINTAINER Marcin Ryzycki marcin@m12.io

RUN yum -y install zsh

RUN wget https://github.com/github/hub/releases/download/v2.2.3/hub-linux-amd64-2.2.3.tgz && \
    tar xvfz hub-linux-amd64-2.2.3.tgz && \
    ln -s /data/www/hub-linux-amd64-2.2.3/bin/hub /usr/local/bin/hub

RUN sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"