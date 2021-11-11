FROM ubuntu:14.04

#Need to install wget & apt-transport-https for https
RUN apt-get update && apt-get install -y wget \
		apt-transport-https

#Import the PGP Key
RUN wget -qO- https://apt.boundlessgeo.com/gpg.key | apt-key add -

#Add the OpenGeo Suite repository
RUN echo "deb https://apt.boundlessgeo.com/suite/latest/ubuntu/ trusty main" > /etc/apt/sources.list.d/opengeo.list

#RUN apt-get update
RUN apt-get update

#Install Complete OpenGeo
RUN apt-get install -y opengeo

#TODO
#Update the Port of tomcat to 80

#TODO
#Update the username & passwords

#Tail the log of tomcat
#CMD ["tail", "-f", "/var/log/tomcat7/catalina.out"]

#Expose Port 8080
EXPOSE 8080
