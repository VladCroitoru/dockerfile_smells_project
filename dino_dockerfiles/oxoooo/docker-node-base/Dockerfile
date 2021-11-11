FROM nginx
MAINTAINER XiNGRZ "chenxingyu92@gmail.com"

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

ENV APP_HOME /var/app
RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

ENV PORT=8000

RUN rm -f /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf

ADD start.sh $APP_HOME
