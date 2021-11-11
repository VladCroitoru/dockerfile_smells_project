FROM ruby:2.1
MAINTAINER Nirmal Pathak <ndpathak@yahoo.com>

RUN cd /root && \
	git clone https://github.com/gmarik/Gistie && \
	cd Gistie && bundle install && \
	rake db:create db:migrate

ADD start.sh /root/Gistie/

EXPOSE 3000
ENTRYPOINT ["/root/Gistie/start.sh"]
