# Container for developing Sass/Scss at Holberton School

FROM holbertonschool/base-ubuntu-1404
MAINTAINER Guillaume Salva <guillaume@holbertonschool.com>

RUN echo 'deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu precise main' >> /etc/apt/sources.list
RUN apt-get update

RUN apt-get install -y curl wget git

RUN apt-get install -y build-essential gcc
RUN apt-get install -y libc6-dev-i386
RUN apt-get install -y libssl-dev

RUN apt-get install -y autogen autoconf libtool

RUN apt-get install -y --force-yes ruby2.3 ruby2.3-dev

RUN gem install sass

ADD run.sh /tmp/run.sh
RUN chmod u+x /tmp/run.sh

# start run!
CMD ["./tmp/run.sh"]
