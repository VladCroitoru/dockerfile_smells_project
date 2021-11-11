FROM ubuntu:14.04.4

ENV DEBIAN_FRONTEND noninteractive

# what and where to install :
ENV JMETER_VERSION 2.13
ENV PLUGINS_VERSION 1.2.0
ENV JMETER_CUR_VER_PATH /usr/local
ENV JMETER_PATH /usr/local/jmeter
ENV PLUGINS_PATH $JMETER_PATH/plugins

# Automagically accept Oracle's license
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

# apt-add-repository requirement and tools:
RUN apt-get update && apt-get -y install software-properties-common python-apt python-simplejson \
    vim curl

# Install java RE for jmeter :
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update && apt-get install -y --force-yes oracle-java8-installer unzip wget

# install requirements for our external jmeter scenario retrieval:
RUN apt-get install -y --allow-unauthenticated git-core ca-certificates

# install apache jmeter from apache.org binary archives:
# /usr/local/apache-jmeter-2.13
# /usr/local/jmeter -> /usr/local/apache-jmeter-2.13
RUN mkdir -p $JMETER_CUR_VER_PATH && \
    cd $JMETER_CUR_VER_PATH && \
    wget -q https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-$JMETER_VERSION.tgz && \
    tar -zxf apache-jmeter-$JMETER_VERSION.tgz && \
    ln -s $JMETER_CUR_VER_PATH/apache-jmeter-$JMETER_VERSION $JMETER_PATH && \
    rm apache-jmeter-$JMETER_VERSION.tgz

# Install JMeterPlugins-ExtrasLibs
RUN mkdir -p $PLUGINS_PATH && \
    wget -q http://jmeter-plugins.org/downloads/file/JMeterPlugins-ExtrasLibs-$PLUGINS_VERSION.zip && \
    unzip -o -d $PLUGINS_PATH JMeterPlugins-ExtrasLibs-$PLUGINS_VERSION.zip && \
    wget -q http://jmeter-plugins.org/downloads/file/JMeterPlugins-Extras-$PLUGINS_VERSION.zip && \
    unzip -o -d $PLUGINS_PATH JMeterPlugins-Extras-$PLUGINS_VERSION.zip && \
    wget -q http://jmeter-plugins.org/downloads/file/JMeterPlugins-Standard-$PLUGINS_VERSION.zip && \
    unzip -o -d $PLUGINS_PATH JMeterPlugins-Standard-$PLUGINS_VERSION.zip

# Copy plugins to jmeter enviroment
RUN cp $PLUGINS_PATH/lib/*.jar $JMETER_CUR_VER_PATH/apache-jmeter-$JMETER_VERSION/lib/
RUN cp $PLUGINS_PATH/lib/ext/*.jar $JMETER_CUR_VER_PATH/apache-jmeter-$JMETER_VERSION/lib/ext/

# Copy user.properties
ADD user.properties $JMETER_CUR_VER_PATH/apache-jmeter-$JMETER_VERSION/bin/

# directory holding our jmeter scenarii files (sent there using ansible)
RUN mkdir -p /etc/jmeter/$JMETER_VERSION/scenarii
