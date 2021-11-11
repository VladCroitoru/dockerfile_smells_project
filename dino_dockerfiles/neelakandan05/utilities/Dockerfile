FROM centos:7

RUN yum -y install openssh-server && \
    yum -y install git && \
    yum -y install docker && \
    yum -y install wget && \
    yum clean all
  
RUN echo "root:password" | chpasswd  
RUN useradd jenkins  

RUN wget -P /opt/ --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz \
    && tar xzf /opt/jdk-8u66-linux-x64.tar.gz -C /opt \
    && rm /opt/jdk-8u66-linux-x64.tar.gz

RUN alternatives --install /usr/bin/java java /opt/jdk1.8.0_66/bin/java 2 \
    && alternatives --install /usr/bin/jar jar /opt/jdk1.8.0_66/bin/jar 2 \
    && alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_66/bin/javac 2 \
    && alternatives --set jar /opt/jdk1.8.0_66/bin/jar \
    && alternatives --set javac /opt/jdk1.8.0_66/bin/javac
    
ENV JAVA_HOME /opt/jdk1.8.0_66
ENV JRE_HOME /opt/jdk1.8.0_66/jre
  
RUN mkdir -p /var/run/sshd  
RUN ssh-keygen -A
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd  
   
EXPOSE 22

RUN ["java","-version"]
CMD ["/usr/sbin/sshd", "-D"] 
