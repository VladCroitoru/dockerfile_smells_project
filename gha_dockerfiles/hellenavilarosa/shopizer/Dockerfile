FROM public.ecr.aws/amazoncorretto/amazoncorretto:latest

ADD sm-core-model/pom.xml sm-core-model/pom.xml
ADD sm-core-modules/pom.xml sm-core-modules/pom.xml
ADD sm-core/pom.xml sm-core/pom.xml
ADD sm-shop-model/pom.xml sm-shop-model/pom.xml
ADD sm-shop/pom.xml sm-shop/pom.xml

RUN yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
RUN yum install -y https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-selinux-17.03.0.ce-1.el7.centos.noarch.rpm
RUN yum install -y https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-17.03.0.ce-1.el7.centos.x86_64.rpm
RUN yum localinstall *rpm

RUN yum install wget -y
RUN wget https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
RUN sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo
RUN yum install -y apache-maven
RUN yum install jq -y
RUN yum install unzip -y

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

COPY pom.xml .
RUN mvn -T 2C dependency:go-offline -B
