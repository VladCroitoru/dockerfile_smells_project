FROM centos:centos6

MAINTAINER Christian Tzolov "https://github.com/tzolov"

USER root

ENV JAVA_HOME /usr/java/jdk1.6.0_45
ENV MAVEN_OPTS -Xmx2g -XX:MaxPermSize=512M -XX:ReservedCodeCacheSize=512m
ENV MAVEN_HOME /usr/local/maven
ENV PATH $PATH:$MAVEN_HOME/bin

ADD spark_assembly.patch /spark_assembly.patch
ADD build_rpm.sh /build_rpm.sh

RUN \
    echo "----------------------------- Install JDK 6, GIT and OS Utilities --------------------------" ;\
    yum -y install git wget which unzip tar ;\
    wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/6u45-b06/jdk-6u45-linux-x64-rpm.bin" ;\
    chmod +x jdk-6u45-linux-x64-rpm.bin ;\
    ./jdk-6u45-linux-x64-rpm.bin ;\
    yum -y install ./jdk-6u45-linux-amd64.rpm ;\
    rm ./jdk-6u45-linux-amd64.rpm ;\
    echo "------------- Install Maven3 ---------------------------------------------------------------" ;\
    curl -o /tmp/maven.tar.gz http://ftp.nluug.nl/internet/apache/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz  ;\
    mkdir $MAVEN_HOME  ;\
    tar -C $MAVEN_HOME -xzvf /tmp/maven.tar.gz --strip 1  ;\
    rm /tmp/maven.tar.gz ;\
    echo "------------- Install Alien ----------------------------------------------------------------" ;\
    rpm -iUvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm ;\
    yum -y install dpkg python rpm-build make m4 gcc-c++ autoconf automake redhat-rpm-config mod_dav_svn mod_ssl mod_wsgi perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker ;\
    git clone git://git.kitenet.net/alien ;\
    cd /alien/; perl Makefile.PL; make; make install; cd / ;\
    rm -Rf /alien ;\
    yum -y erase perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker gcc-c++ m4 autoconf automake ;\      
    echo "------------- Clone Spark Git Repo and (pre)download some Maven dependencies ---------------" ;\
    cd / ;\
    git clone https://github.com/apache/spark.git ;\
    cd /spark ;\
    mvn -Pyarn -Phadoop-2.2 -Pdeb -Dhadoop.version=2.2.0 -DskipTests -Ddeb.bin.filemode=755 clean package ;\
    mvn -Pyarn -Phadoop-2.2 -Pdeb -Dhadoop.version=2.2.0-gphd-3.1.0.0 -DskipTests -Ddeb.bin.filemode=755 clean package ;\    
    echo "------------- Configure the build utilities ------------------------------------------------" ;\      
    chmod a+x /build_rpm.sh 
# END RUN

# Sink with the Spark git repo
WORKDIR /spark

# Sync with the git master repo
CMD git pull --rebase
