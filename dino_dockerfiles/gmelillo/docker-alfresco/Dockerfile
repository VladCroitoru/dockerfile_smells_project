FROM ubuntu:21.04
MAINTAINER Gabriel Melillo "gabriel@melillo.me"

RUN apt-get update && apt-get -y upgrade && apt-get install locales
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales

RUN echo "Europe/Berlin" > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get -y install openjdk-7-jdk wget

RUN wget -O alfresco-community-5.0.b-installer-linux-x64.bin \
	http://dl.alfresco.com/release/community/5.0.d-build-00002/alfresco-community-5.0.d-installer-linux-x64.bin
RUN chmod +x alfresco-community-5.0.b-installer-linux-x64.bin

RUN ./alfresco-community-5.0.b-installer-linux-x64.bin \
	--mode text \
	--installer-language en \
	--baseunixservice_install_as_service 1 \
	--alfresco_admin_password AlfrescoAdmin

EXPOSE 80
EXPOSE 21
EXPOSE 139
EXPOSE 445
EXPOSE 7070
EXPOSE 8009
EXPOSE 8080
EXPOSE 8443

CMD service alfresco start && /bin/sh -c "while true;do sleep 1;done"

