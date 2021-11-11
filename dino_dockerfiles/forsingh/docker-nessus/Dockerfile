FROM centos:7
RUN yum update -y
RUN yum install -y wget 
    
RUN wget -O /tmp/Nessus-6.9.2-es7.x86_64.rpm \
    "https://s3.ap-south-1.amazonaws.com/innodemo/Nessus-6.9.2-es7.x86_64.rpm"
RUN yum localinstall /tmp/Nessus-6.9.2-es7.x86_64.rpm  -y

#Removing tools used for debugging 
#RUN yum install -y net-tools
   
EXPOSE 8834

ENTRYPOINT [ "/opt/nessus/sbin/nessusd" ]
