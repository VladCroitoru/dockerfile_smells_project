FROM ubuntu:14.04
# maintainer details
MAINTAINER Alexandre Combe "aco@yooz.fr"

RUN echo deb http://archive.ubuntu.com/ubuntu trusty main universe > /etc/apt/sources.list

RUN apt-get update
RUN apt-get upgrade -y

# SSH and other tools
RUN apt-get install -y openssh-server supervisor curl unzip
RUN mkdir -p /var/run/sshd
ADD ssh/authorized_keys /root/.ssh/authorized_keys
RUN sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional pam_loginuid.so/g' /etc/pam.d/sshd
RUN mkdir -p /var/log/supervisor

# Jenkins
RUN curl http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list
RUN apt-get update
# HACK: https://issues.jenkins-ci.org/browse/JENKINS-20407
RUN mkdir /var/run/jenkins
RUN apt-get install -y jenkins
# Allow local jenkins to connect to localhost git repo
ADD ssh/id_rsa /root/.ssh/
RUN chmod 0600 /root/.ssh/id_rsa
ADD ssh/id_rsa.pub /root/.ssh/
ADD ssh/known_hosts /root/.ssh/

# Sonar
RUN curl --remote-name http://dist.sonar.codehaus.org/sonarqube-4.1.zip
RUN unzip sonarqube-4.1.zip
RUN mv sonarqube-4.1 /opt
RUN rm -f sonarqube-4.1.zip

# Git
RUN apt-get install -y git
# Clone and init repo for course
RUN git clone https://github.com/acombe/source-code-practice-course
# Work branch creation because student can't push on master (wich is not a bare repo, we just clone it from github...)
RUN cd /source-code-practice-course/ && git checkout -b work

# Maven
# RUN apt-get install -y maven => error "fuse install device"
RUN curl --remote-name http://mir2.ovh.net/ftp.apache.org/dist/maven/maven-3/3.2.1/binaries/apache-maven-3.2.1-bin.zip
RUN unzip apache-maven-3.2.1-bin.zip
RUN mv apache-maven-3.2.1 /opt/
RUN rm -f apache-maven-3.2.1-bin.zip
RUN ln -s /opt/apache-maven-3.2.1/bin/mvn /usr/bin/mvn
RUN sed -i '1iM3_HOME="/opt/apache-maven-3.2.1"' /etc/environment
RUN sed -i '1iM3="$M3_HOME/bin"' /etc/environment

# Oracle JDK 7
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:webupd8team/java -y
RUN apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java7-installer
RUN sed -i '1iJAVA_HOME="/usr/lib/jvm/java-7-oracle/"' /etc/environment

# Apache
RUN apt-get -y install apache2 libapache2-mod-php5 php5
RUN rm -rf /var/www/*
RUN mkdir -p /var/www/html/images
RUN mkdir -p /var/www/html/documents
ADD html/index.php /var/www/html/
ADD html/images/ /var/www/html/images/
ADD html/documents/ /var/www/html/documents/

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80 22 8080 9000
CMD ["/usr/bin/supervisord"]