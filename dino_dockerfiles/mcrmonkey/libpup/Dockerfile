FROM debian:stretch

LABEL MAINTAINER ant <git@manchestermonkey.co.uk>

RUN apt-get update -qq && apt-get install -qq git ruby rubygems && \
	gem install puppet --no-ri --no-rdoc && \
	gem install librarian-puppet --no-ri --no-rdoc && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /etc/puppet

ENTRYPOINT ["librarian-puppet"]

CMD ["install"]
