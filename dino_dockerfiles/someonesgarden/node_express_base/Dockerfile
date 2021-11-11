FROM node:argon

MAINTAINER 0.1 Daisuke Nishimura d@someonesgarden.org

RUN groupadd -r express && useradd -r -g express express

#apt-get
RUN apt-get update && \
apt-get install -y \
vim \
libfreetype6-dev \
libfontconfig1-dev \
wget \
bzip2 \
git \
python \
unifont


# Install JRE + JDK
#ENV JAVA_HOME=/usr/lib/jvm/default-java
#ENV PATH=$JAVA_HOME/bin:$PATH

#RUN apt-get update -y && \
#apt-get install default-jre -y && \
#apt-get install  default-jdk -y

#RUN \
#    echo "===> add webupd8 repository..."  && \
#    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list  && \
#    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  && \
#    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  && \
#    apt-get update  && \
#    \
#    \
#    echo "===> install Java"  && \
#    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
#    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
#    DEBIAN_FRONTEND=noninteractive  apt-get install -y --force-yes oracle-java8-installer oracle-java8-set-default  && \
#    \
#    \
#    echo "===> clean up..."  && \
#    rm -rf /var/cache/oracle-jdk8-installer  && \
#    apt-get clean  && \
#    rm -rf /var/lib/apt/lists/*


#Create app directory
# Install app dependencies
RUN mkdir -p /usr/src/app
COPY package.json /usr/src/app/

WORKDIR /usr/src/app
RUN npm install && npm update -g
RUN npm install -g bower grunt-cli coffee-script && \
echo '{ "allow_root": true }' > /root/.bowerrc

WORKDIR /usr/src/app/public
RUN bower install backbone underscore jquery  --save
RUN bower install glyphicons glyphicons-halflings --save
RUN bower install bootstrap --save
#RUN bower install angular angular-material \
#angular-messages angular-route \
#angular-resource angular-sanitize \
#angular-local-storage --save
#RUN bower install d3 --save

COPY . /usr/src/app
WORKDIR /usr/src/app

#EXPOSE 8080

#CMD [ "npm", "start" ]
#CMD [ "coffee", "bin/www.coffee" ]


