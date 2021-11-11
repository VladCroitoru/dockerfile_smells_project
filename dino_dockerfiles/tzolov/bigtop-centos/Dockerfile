FROM centos:centos6

MAINTAINER Christian Tzolov "https://github.com/tzolov"

RUN echo "---------------------- Create sudo & paswordless 'bigtop' user -----" ;\
   yum -y install sudo ;\
   useradd bigtop && echo "bigtop:bigtop" | chpasswd && gpasswd -a bigtop wheel ;\
   mkdir -p /home/bigtop && chown -R bigtop:bigtop /home/bigtop ;\
   sed -i "s/Defaults    requiretty.*/# Defaults    requiretty/g" /etc/sudoers ;\
   echo '%wheel        ALL=(ALL)       NOPASSWD: ALL' >> /etc/sudoers

USER bigtop

ENV JAVA_HOME /usr/java/jdk1.7.0_65
ENV JAVA5_HOME /usr/java/jdk1.7.0_65
ENV JVM_ARGS -Xmx2g -XX:MaxPermSize=512M -XX:ReservedCodeCacheSize=512m
ENV MAVEN_HOME /opt/apache-maven-3.3.3
ENV MAVEN_OPTS -Xmx2g -XX:MaxPermSize=512M -XX:ReservedCodeCacheSize=512m
ENV ANT_HOME /opt/apache-ant
ENV SCALA_HOME /usr/share/scala
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:$MAVEN_HOME/bin:$ANT_HOME/bin
ENV FORREST_HOME /opt/apache-forrest-0.9

RUN cd ~ ;\
echo "----------------------------- Install required packages ------------" ;\
   sudo yum -y install wget tar git subversion gcc gcc-c++ make cmake fuse autoconf automake libtool sharutils xmlto ;\
   sudo yum -y install lzo-devel zlib-devel fuse-devel openssl-devel python-devel libxml2-devel libxslt-devel cyrus-sasl-devel sqlite-devel mysql-devel openldap-devel rpm-build createrepo redhat-rpm-config ;\
   sudo yum -y install python-setuptools asciidoc libyaml-devel cppunit-devel ;\
echo "----------------------------- Install JDK --------------------------" ;\  
   wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.rpm" ;\
   sudo yum -y install ./jdk-7u65-linux-x64.rpm; java -version ;\
   rm ./jdk-7u65-linux-x64.rpm ;\ 
echo "----------------------------- Install Scala --------------------------" ;\      
   sudo yum -y install http://www.scala-lang.org/files/archive/scala-2.11.5.rpm ;\
echo "----------------------------- Install Maven --------------------------" ;\
   wget http://ftp.nluug.nl/internet/apache/maven/maven-3/3.3.3/binaries/apache-maven-3.3.3-bin.tar.gz ;\
   tar -xzvf apache-maven-3.3.3-bin.tar.gz ;\
   sudo mv apache-maven-3.3.3 /opt/ ;\
   rm apache-maven-3.3.3-bin.tar.gz ;\
echo "----------------------------- Install Ant ---------------------------" ;\
   wget http://archive.apache.org/dist/ant/binaries/apache-ant-1.9.4-bin.tar.gz ;\
   tar -xvzf apache-ant-1.9.4-bin.tar.gz ;\
   sudo mv apache-ant-1.9.4 /opt/apache-ant ;\
   rm apache-ant-1.9.4-bin.tar.gz ;\
echo "----------------------------- Install Forrest ----------------------" ;\
   wget http://archive.apache.org/dist/forrest/0.9/apache-forrest-0.9.tar.gz ;\
   tar -xzvf apache-forrest-0.9.tar.gz ;\
   sed -i 's/property name="forrest.validate.sitemap" value="${forrest.validate}"/property name="forrest.validate.sitemap" value="false"/g' apache-forrest-0.9/main/targets/validate.xml ;\
   sed -i 's/property name="forrest.validate.stylesheets" value="${forrest.validate}"/property name="forrest.validate.stylesheets" value="false"/g' apache-forrest-0.9/main/targets/validate.xml ;\
   sed -i 's/property name="forrest.validate.stylesheets.failonerror" value="${forrest.validate.failonerror}"/property name="forrest.validate.stylesheets.failonerror" value="false"/g' apache-forrest-0.9/main/targets/validate.xml ;\
   sed -i 's/property name="forrest.validate.skins.stylesheets" value="${forrest.validate.skins}"/property name="forrest.validate.skins.stylesheets" value="false"/g' apache-forrest-0.9/main/targets/validate.xml ;\
   sudo mv apache-forrest-0.9 /opt/ ;\
   rm apache-forrest-0.9.tar.gz ;\
echo "----------------------------- Install Protobuf ---------------------" ;\
   wget http://protobuf.googlecode.com/files/protobuf-2.5.0.tar.bz2 ;\
   tar -xvf protobuf-2.5.0.tar.bz2 ;\
   cd protobuf-2.5.0 ;\
   ./configure --prefix=/usr ;\
   make ;\
   sudo make install ;\
   sudo ldconfig ;\
   cd ~ ;\
echo "----------------------------- Install SSH Keys ---------------------" ;\
   ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa ;\
   cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys ;\
echo "----------------------------- Clone Bigtop -------------------------" ;\
   git clone https://github.com/apache/bigtop.git ;\
   sudo chown -R bigtop:bigtop bigtop ;\
   cd bigtop ;\
   git checkout HEAD ;\
   ls -lah ;\

#   git clone https://github.com/apache/bigtop.git ;\


