FROM ubuntu:bionic

RUN apt-get update && apt-get install -y sudo openssh-server nginx

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test 

RUN  echo 'test:test' | chpasswd

RUN service ssh start

EXPOSE 22
EXPOSE 80

CMD ["/usr/sbin/sshd","-D"]
