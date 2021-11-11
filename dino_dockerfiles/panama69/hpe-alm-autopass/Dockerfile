#Pulling this version as the latest will change and wanted to ensure a stable starting point
#you should be able to remove the tag and things work so long as that version of CentOS is
#supported by HPE AutoPass
FROM centos:centos7.2.1511

LABEL name="CentOS Base Image"
LABEL vendor="CentOS"
LABEL license=GPLv2

#use the COPY option if the URL is down or you don't wish to pull from external
#As of 11/Jul/2016, the URL points to AutoPass 9.1
#ADD http://flynnshome.com/downloads/setupAutoPass.bin /tmp/setupAutoPass.bin
#COPY ./setupAutoPass.bin /tmp/setupAutoPass.bin
ADD http://flynnshome.com/downloads/setupAutoPass9.3.bin /tmp/setupAutoPass.bin

RUN chmod 777 /tmp/setupAutoPass.bin;
RUN /tmp/setupAutoPass.bin -i silent;
RUN rm -f /tmp/setupAutoPass.bin

WORKDIR "/opt/HP/HP AutoPass License Server/HP AutoPass License Server/HP AutoPass License Server/bin/"
ENV PATH /opt/HP/HP AutoPass License Server/HP AutoPass License Server/HP AutoPass License Server/bin/:$PATH

#following line works on CentOs but doesn't keep the container up on Ubuntu 14.04LTS
#CMD bash -c 'hpLicenseServer start';'bash';

#added this line to keep the container up.
#you must use docker exec -it <container name> bash to be able to connect, exit AND have the container remain running.
CMD bash -c 'hpLicenseServer start;tail -f ../logs/catalina.out'

EXPOSE 5814
