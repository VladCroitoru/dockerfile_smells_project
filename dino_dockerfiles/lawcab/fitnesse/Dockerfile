FROM lawcab/baseimage
MAINTAINER Lawrence Cabal <lawcab@gmail.com>

# Add PHP5.6 Repo
RUN add-apt-repository -y ppa:ondrej/php
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
RUN apt-get -yqq update
RUN apt-get install -yqq php5.6
RUN apt-get install -yqq php5.6-bcmath php5.6-bz2 php5.6-curl php5.6-dba
RUN apt-get install -yqq php5.6-mbstring php5.6-mysql php5.6-xml php5.6-soap php5.6-zip php-xcache php-propro php-raphf

#install jdk
RUN mkdir /usr/local/java \
&& cd /usr/local/java \
&& wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.tar.gz \
&& sudo tar xvzf jdk-8u111-linux-x64.tar.gz \
&& echo 'JAVA_HOME=/usr/local/java/jdk1.8.0_111' >> /etc/profile \
&& echo 'PATH=$PATH:$HOME/bin:$JAVA_HOME/bin' >> /etc/profile \
&& echo 'export JAVA_HOME' >> /etc/profile \
&& echo 'export PATH' >> /etc/profile 
RUN  update-alternatives --install "/usr/bin/java" "java" "/usr/local/java/jdk1.8.0_111/bin/java" 1 \
&& update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/local/java/jdk1.8.0_111/bin/javaws" 1 \
&& update-alternatives --set java /usr/local/java/jdk1.8.0_111/bin/java \
&& update-alternatives --set javaws /usr/local/java/jdk1.8.0_111/bin/javaws
	
#install fitnesse and phpslim
RUN wget http://github.com/downloads/ggramlich/phpslim/phpslim.phar 
RUN wget "http://fitnesse.org/fitnesse-standalone.jar?responder=releaseDownload&release=20160618"
RUN mv "fitnesse-standalone.jar?responder=releaseDownload&release=20160618" "fitnesse-standalone.jar"
RUN mv phpslim.phar /opt
RUN mkdir /usr/local/fitnesse
RUN mv fitnesse-standalone.jar /usr/local/fitnesse
RUN mkdir /prj