FROM jenkins/jenkins:lts

MAINTAINER anyei <angelyoelroblesmercedes@gmail.com>

#Star me or leave any comment here: https://hub.docker.com/r/anyei/jenkins-to-salesforce/
#Please report issues here : https://github.com/anyei/jenkins-to-salesforce/issues


#Changing to root, it was running on jenkins user context
USER root


#INSTALLING ANT

RUN mkdir -p /var/ant_home

ADD http://ftp.wayne.edu/apache/ant/binaries/apache-ant-1.10.6-bin.zip /var/ant_home/apache-ant-1.10.6-bin.zip 

RUN unzip /var/ant_home/apache-ant-1.10.6-bin.zip -d /var/ant_home && rm /var/ant_home/apache-ant-1.10.6-bin.zip

ENV ANT_HOME=/var/ant_home/apache-ant-1.10.6

ENV PATH=${PATH}:${ANT_HOME}/bin

#In case anyone is intersted, the following command would retreive additional ant's plugins
#RUN ant -f ${ANT_HOME}/fetch.xml -Ddest=sytem

#INSTALLING ANT BUILD.XML TEMPLATE FOR SALESFORCE PLUGIN

RUN mkdir -p /var/ant_home/build_template/

ADD tools/buildTemplate.xml /var/ant_home/build_template/build_template.xml

ENV SFDC_BUILD_TEMPLATE=/var/ant_home/build_template/

ENV PATH=${PATH}:${SFDC_BUILD_TEMPLATE}

#INSTALL add_run_tests.sh

ADD tools/add_run_tests.sh /usr/bin/get_build_template

RUN chmod +x /usr/bin/get_build_template

#INSTALL initial.sh

ADD tools/initial.sh /usr/bin/initial

RUN chmod +x /usr/bin/initial

#INSTALLING SALESFORCE ANT PLUGIN
RUN mkdir ${ANT_HOME}/lib/x

ADD https://gs0.salesforce.com/dwnld/SfdcAnt/salesforce_ant_48.0.zip ${ANT_HOME}/lib/x/salesforce_ant_48.0.zip
#https://na17.salesforce.com/dwnld/SfdcAnt/salesforce_ant_34.0.zip ${ANT_HOME}/lib/x/salesforce_ant_34.0.zip

RUN unzip ${ANT_HOME}/lib/x/salesforce_ant_48.0.zip -d ${ANT_HOME}/lib/x && cp ${ANT_HOME}/lib/x/ant-salesforce.jar ${ANT_HOME}/lib/ant-salesforce.jar && rm -rf ${ANT_HOME}/x

RUN chown -R jenkins "${ANT_HOME}" /usr/bin/get_build_template

RUN apt update && apt -y install sudo \ 
   && sed -i "2 iexport JAVA_HOME=${JAVA_HOME}" /etc/ca-certificates/update.d/docker-openjdk \
   && echo 'jenkins ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/jenkins
#Changing to jenkins user
USER jenkins

ENTRYPOINT ["initial"]

