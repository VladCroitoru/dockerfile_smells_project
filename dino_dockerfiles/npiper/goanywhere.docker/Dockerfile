FROM centos:7

RUN yum -y -q install java-1.8.0-openjdk-devel
RUN yum install -y -q nmap gunzip which curl

RUN mkdir -p /etc/fonts
COPY local.conf /etc/fonts/local.conf 


RUN mkdir -p /home/vagrant
RUN curl -L https://s3.eu-west-2.amazonaws.com/binaries.dev.neilpiper.me/ga5_5_8_linux_x64.sh > /home/vagrant/ga5_5_8_linux_x64.sh

RUN chmod +x /home/vagrant/ga5_5_8_linux_x64.sh

RUN printf 'o\n\n\n\n\n1\n/home/vagrant/Linoma_Software/\n8000\n8001\n1443\n2221\n1990\n2222\n8010\n8009\n8005\n' | /home/vagrant/ga5_5_8_linux_x64.sh -c

COPY goanywhere.service /usr/lib/systemd/system/goanywhere.service

WORKDIR /home/vagrant/Linoma_Software 

# Administration Port
EXPOSE 8000

# Secure Administration Port
EXPOSE 8001

# HTTPS Service Port
EXPOSE 443

# FTP Service Port
EXPOSE 21

# FTPS Service Port
EXPOSE 990

# SFTP Service Port
EXPOSE 22

# GoFast Service Port
EXPOSE 8010

# Agents Service Port
EXPOSE 8009

# Shutdown Port
EXPOSE 8005

CMD ["goanywhere.sh","start"]
