FROM ruby:2.3

MAINTAINER Peter Esselius <pepp@me.com>

# Need apt-transport-https installed in order to install docker
RUN apt-get update && \
		apt-get install -y apt-transport-https && \
		apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
		echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list && \
		apt-get update && \
		apt-get install -y docker-engine

COPY fluent.conf /etc/fluent/fluent.conf

WORKDIR /tmp
COPY Gemfile* /tmp/
RUN bundle install

COPY startup.sh /tmp/
RUN chmod +x /tmp/startup.sh

CMD ["/tmp/startup.sh"]
