FROM node
MAINTAINER mark<mark.oliver.schmitt@gmail.com>

# openssh for jenkins, openjre for jenkins slave. this prevents the jenkins setup to download this every time
RUN apt-get update && apt-get install -y openssh-server openjdk-7-jre-headless && apt-get clean

RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\
  echo "jenkins:jenkins" | chpasswd

EXPOSE 22

RUN mkdir /var/run/sshd

CMD ["/usr/sbin/sshd", "-D"]
