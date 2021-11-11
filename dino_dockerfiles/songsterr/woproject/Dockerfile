FROM anapsix/alpine-java:jdk7
MAINTAINER Aleksey Potapkin <apotapkin@demax.ru>

RUN apk add --no-cache curl

# Installs Ant
ENV ANT_VERSION 1.9.7
RUN cd && \
    wget -q http://www.us.apache.org/dist/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz && \
    tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \
    mv apache-ant-${ANT_VERSION} /opt/ant && \
    rm apache-ant-${ANT_VERSION}-bin.tar.gz
ENV ANT_HOME /opt/ant
ENV PATH ${PATH}:/opt/ant/bin

COPY ./WOJenkins/ /WOJenkins
COPY ./wonder/ /wonder

ENV WO_VERSION 5.4.3
ENV WONDER_BRANCH wonder_6

COPY WOInstaller.jar /WOFrameworksRepository/WebObjects/
# Ant tasks jar 
COPY woproject.jar /WOFrameworksRepository/WOProject/

RUN bash -x /WOJenkins/Install/WebObjects/installWebObjects.sh && \
bash -x /WOJenkins/Build/Wonder/WorkspaceSetupScripts/Git/setupWonderWorkspace.sh

RUN ant frameworks frameworks.install \
	-propertyfile /Root/build.properties \
	-Dant.build.javac.target=1.5 \
	-buildfile wonder/build.xml

RUN apk del curl

COPY build-wocore.xml /root/Library/
COPY wobuild.properties /root/Library/

RUN ln -snf /Root/jenkins.build.properties /root/build.properties 

RUN mkdir /Projects
