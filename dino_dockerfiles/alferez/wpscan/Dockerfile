FROM ruby:latest
MAINTAINER Jose A Alferez <correo@alferez.es>

RUN mkdir /scripts
WORKDIR /scripts
ADD ./wpscan /scripts/wpscan

WORKDIR /scripts/wpscan
RUN bundle install
RUN chmod +x /scripts/wpscan/*.rb
RUN ./wpscan.rb --update
RUN echo "#! /bin/bash" >> /wpscan.sh
RUN echo "/scripts/wpscan/wpscan.rb --update >/dev/null" >> /wpscan.sh
RUN echo '/scripts/wpscan/wpscan.rb --follow-redirection --user-agent "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0" -v -e vp,vt --url $1'  >> /wpscan.sh
RUN chmod 777 /wpscan.sh
CMD echo "Use docker run --rm -ti alferez/wpscan /wpscan.sh DOMAIN.COM"

