FROM centos:latest

RUN yum install wget -y
RUN wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
RUN rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
RUN yum install python3 -y
RUN yum install git -y
RUN yum install java-11-openjdk.x86_64 -y
RUN yum install jenkins -y --nobest
RUN yum install sudo -y
COPY Emailsnd.py /
RUN echo -e "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
EXPOSE 8080

CMD ["java","-jar","/usr/lib/jenkins/jenkins.war"]
