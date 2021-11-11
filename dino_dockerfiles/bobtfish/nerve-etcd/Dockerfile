FROM ubuntu:precise
MAINTAINER bobtfish@bobtfish.net

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq -y && \
    apt-get install -qq -y ruby1.9.3 ruby-bundler build-essential git-core iputils-ping && \
    apt-get clean

RUN git clone https://github.com/bobtfish/nerve.git;cd nerve;gem build *.gemspec;gem install *.gem;cd .. ; rm -r nerve

ADD /nerve.conf.json /nerve.conf.json
ADD /run.sh /run.sh
RUN chmod 755 /*.sh; mkdir /nerve_services

ENTRYPOINT ["/run.sh"]
CMD ["run"]

