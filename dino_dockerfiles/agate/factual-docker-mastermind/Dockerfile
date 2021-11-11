FROM openjdk:8

MAINTAINER agate<agate.hao@gmail.com>

RUN apt-get update
RUN apt-get install -y s3cmd logrotate cron
RUN apt-get install -y byobu vim-nox bash-completion sudo openssh-server

RUN adduser --disabled-password --gecos 'mastermind user' mastermind

RUN curl -s https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein > /usr/local/bin/lein
RUN chmod a+x /usr/local/bin/lein
RUN su -c "lein version" - mastermind

ADD bootstrap.sh /bootstrap.sh
CMD /bootstrap.sh

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
