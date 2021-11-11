FROM ubuntu:14.04

MAINTAINER manuel.vacelet@enalean.com

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get -y install jq

# Nginx
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update
RUN apt-get install -y nginx

ADD nginx.conf /etc/nginx/nginx.conf
ADD docker-reverseproxy /etc/nginx/sites-enabled/default

RUN apt-get -y install curl

ADD . /app
WORKDIR /app

CMD ["./run.sh"]
