FROM ubuntu

MAINTAINER Bernardo Dias "bdias.ti@gmail.com"

ENV REFRESHED_AT 2015-25-12

RUN apt-get -yq update && apt-get -yq upgrade

#Install pre-requisites
RUN sudo apt-get -yq install python-software-properties software-properties-common \
                      python g++ make git ruby-compass libfreetype6
					  
#Install curl
RUN sudo apt-get install -y curl

#Add repository
RUN sudo curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -

#Install node
RUN sudo apt-get install -y nodejs

#Install Yeoman, bower and grunt
RUN sudo npm install --global yo bower grunt-cli

#Create user yeoman.
RUN adduser --disabled-password --gecos "" yeoman; \
  echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

#Home defalult
ENV HOME /home/yeoman

EXPOSE 9000

#Change user yeoman
USER yeoman

#Create project folder
RUN mkdir /home/yeoman/yeoman-app

#Set workdir 
WORKDIR /home/yeoman/yeoman-app

#Copy files project from host for container
COPY ./yeoman-app .

#Resolve dependencies
RUN bower -y install
RUN sudo npm install 

CMD sudo grunt serve


