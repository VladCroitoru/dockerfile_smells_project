FROM ubuntu
MAINTAINER hobbyqhd “liubingxin1030@outlook.com”
ENV REFRESHED_AT 2017_08_02
RUN apt-get -yqq update
RUN apt-get -yqq install gcc ruby ruby-dev make nodejs
RUN gem install --no-rdoc --no-ri jekyll -v 2.5.3
VOLUME /data
VOLUME /var/www/html
WORKDIR /data
ENTRYPOINT [ "jekyll", "build", "--destination=/var/www/html" ]
