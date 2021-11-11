# base tomcat image
FROM tomcat

# update source
RUN apt-get update

# Install JDK
RUN apt-get install -y default-jdk
# RUN wget --no-cookies --no-check-certificate --header "Cookie:gpw_e24=http%3a%2f%2fwww.oracle.com%2ftechnetwork%2fjava%2fjavase%2fdownloads%2fjdk8-downloads-2133151.html;oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u71-b15/jdk-8u71-linux-x64.tar.gz

RUN find -name jdk-8u71-linux-x64.tar.gz
RUN cd /usr/lib \
mkdir jvm

RUN tar -xzf ./jdk-8u71-linux-x64.tar.gz -C /usr/lib/jvm/

#ADD jdk-8u71-linux-x64.gz /usr/lib/jvm

# Install subversion
RUN apt-get install -y subversion

# Install maven
RUN wget http://mirrors.hust.edu.cn/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz
RUN tar -xzf ./apache-maven-3.3.9-bin.tar.gz -C /usr/local/


#update code and build
RUN svn checkout svn://115.29.113.90/server_patch_0816 --username steven --password sunbbs99

#RUN ls /usr/local/
#RUN tar -xzf /usr/local/apache-maven-3.3.9-bin.tar.gz
Env JAVA_HOME /usr/lib/jvm/jdk1.8.0_71
ENV M2_HOME /usr/local/apache-maven-3.3.9
ENV PATH $PATH:$M2_HOME/bin:$JAVA_HOME/bin


ADD mavenbuild.sh .
RUN ls
RUN sh mavenbuild.sh

#RUN cd /usr/local/tomcat/server_patch_0816/target/ \
RUN ls /usr/local/tomcat/server_patch_0816/target/

RUN cp /usr/local/tomcat/server_patch_0816/target/SpringMVC.war /usr/local/tomcat/webapps/

RUN echo "root:123456" | chpasswd 

RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd


# 容器需要开放SSH 22端口
EXPOSE 22

# 容器需要开放Tomcat 8080端口
EXPOSE 8080
