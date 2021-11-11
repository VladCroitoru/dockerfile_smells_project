FROM centos:centos6

MAINTAINER Sante Paciello <essebyte@gmail.com>

#Config vars
ENV JAVA_VER=8u172
ENV ANT_VER=1.9.3
ENV RUBY_MAJOR=1.9
ENV RUBY_VERSION=1.9.3-p550
ENV SENCHA_VER=4.0.0.203

#Environment VAR
ENV ANT_HOME=/opt/ant
ENV JAVA_HOME=/opt/java
ENV GEM_HOME=/usr/local/bundle
ENV SENCHA_HOME=/opt/Sencha/Cmd

#Add to PATH variable
ENV PATH $PATH:${JAVA_HOME}/bin:${SENCHA_HOME}

#Update git repo
#RUN yum -y install http://opensource.wandisco.com/centos/6/git/x86_64/wandisco-git-release-6-1.noarch.rpm

RUN yum -y update; yum -y install \
	unzip wget curl tar git \
	openssl-devel bzip2 && yum clean all

# Install Oracle Java8 - BIN
RUN wget http://10.49.2.235/tarfiles/jdk-8u172-linux-x64.tar.gz && \
	tar -xvf jdk-${JAVA_VER}-linux-x64.tar.gz && \
	rm jdk*.tar.gz && \
	mv jdk* ${JAVA_HOME}

#Install ANT
RUN wget http://archive.apache.org/dist/ant/binaries/apache-ant-${ANT_VER}-bin.zip; \
	unzip apache-ant-${ANT_VER}-bin.zip; mv apache-ant-${ANT_VER}/ ${ANT_HOME}; ln -s ${ANT_HOME}/bin/ant /usr/bin/ant; rm -rf apache-ant-${ANT_VER}-bin.zip

#Install correct version of Ruby
RUN curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -
RUN curl -L get.rvm.io | bash -s stable
RUN source /etc/profile.d/rvm.sh
RUN /bin/bash -l -c "rvm requirements"
RUN /bin/bash -l -c "rvm install ruby 1.9.3"
RUN /bin/bash -l -c "rvm use 1.9.3 --default"

#Install compass from via gem
RUN /bin/bash -l -c "gem install compass"

# Install Sencha-CMD
RUN \
    wget -O sencha-cmd.zip https://cdn.sencha.com/cmd/${SENCHA_VER}/SenchaCmd-${SENCHA_VER}-linux-x64.run.zip && \
    unzip sencha-cmd.zip && rm sencha-cmd.zip && chmod +x SenchaCmd-${SENCHA_VER}-linux-x64.run && \
    mkdir -p ${SENCHA_HOME} && mv SenchaCmd-${SENCHA_VER}-linux-x64.run ${SENCHA_HOME} && \
    ${SENCHA_HOME}/SenchaCmd-${SENCHA_VER}-linux-x64.run --prefix /opt --mode unattended  && \
    rm ${SENCHA_HOME}/SenchaCmd-${SENCHA_VER}-linux-x64.run

