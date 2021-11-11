FROM ubuntu:14.04

MAINTAINER Niclas Ahlstrand <niclas.ahlstrand@pensionsmyndigheten.se>

# Add a "Message of the Day" to help identify container when logging in via SSH
RUN echo '[ Ubuntu 14.04 PM ]' > /etc/motd

# Install some software...
RUN echo 'root:ubuntu' | chpasswd

# SSH 
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -i 's/#UsePAM yes/UsePAM no/g'  /etc/ssh/sshd_config

# Change characterset to ISO-8859-15
RUN locale-gen "en_US.ISO-8859-15"
RUN echo "dpkg-reconfigure locales"
RUN echo 'export LC_ALL="en_US.ISO-8859-15"' >> /etc/profile

EXPOSE 22


CMD /usr/sbin/sshd -D
