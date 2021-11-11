# Browser over SSH
#
# VERSION               0.1
# Supports Firefox, Google Chrome, and Flash
# Run with: docker run -rm -t -i magglass1/docker-browser-over-ssh

FROM fedora

# Install updates and required base packages
RUN yum update -y
RUN yum install wget -y
RUN yum groupinstall fonts -y

# Install Adobe repository
RUN yum install http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm -y
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux

# Install Google Chrome repository
ADD google-chrome.repo /etc/yum.repos.d/ 
RUN wget -q https://dl-ssl.google.com/linux/linux_signing_key.pub
RUN rpm --import linux_signing_key.pub
RUN rm linux_signing_key.pub

# Install Firefox, Chrome, SSHD, and other required packages
RUN yum install firefox flash-plugin google-chrome-stable openssh-server xorg-x11-xauth pwgen -y

# Initialize SSHD and create the webuser user
RUN sshd-keygen
RUN useradd webuser

EXPOSE 22
CMD echo -n "Initializing..."; IP=$(hostname -i); PW=$(pwgen -s 16 1); echo "$PW" | passwd --stdin webuser > /dev/null; echo -e "\r               \rIP address:\t$IP\nPassword:\t$PW\nFirefox:\tssh -X webuser@$IP firefox\nGoogle Chrome:\tssh -X webuser@$IP google-chrome --no-sandbox"; /usr/sbin/sshd -D
