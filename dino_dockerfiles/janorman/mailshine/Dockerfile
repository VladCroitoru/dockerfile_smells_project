FROM ubuntu:latest
MAINTAINER James Norman (JANorman)

## Update the OS
RUN apt-get update -y
RUN apt-get install ruby-full build-essential libxml2 -y 

## Add the framework
RUN gem install sinatra
RUN gem install thin
RUN gem install json
RUN gem install premailer
RUN gem install hpricot

## Add files
RUN mkdir /home/app
ADD src/ /home/app

EXPOSE 4567
CMD ruby /home/app/app.rb