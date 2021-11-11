FROM jenkins

USER root
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -
RUN apt-get update && apt-get install -y nodejs
RUN npm install -g grunt-cli

# set shell variables for java installation
ENV java_version 1.8.0_11
ENV filename jdk-8u11-linux-x64.tar.gz
ENV downloadlink http://download.oracle.com/otn-pub/java/jdk/8u11-b12/$filename

# download java, accepting the license agreement
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /tmp/$filename $downloadlink

# unpack java
RUN mkdir /opt/java-oracle && tar -zxf /tmp/$filename -C /opt/java-oracle/
ENV JAVA_HOME /opt/java-oracle/jdk$java_version
ENV PATH $JAVA_HOME/bin:$PATH

# configure symbolic links for the java and javac executables
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000 && update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 20000

COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt

RUN mkdir /var/jenkins_home/.gradle
COPY gradle.properties /var/jenkins_home/.gradle/
USER jenkins

