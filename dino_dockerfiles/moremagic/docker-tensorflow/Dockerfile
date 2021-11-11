FROM ubuntu:15.04
MAINTAINER moremagic <itoumagic@gmail.com>

RUN apt-get update && apt-get install -y openssh-server openssh-client
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN apt-get install -y wget curl git python python-dev build-essential
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python
RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.6.0-cp27-none-linux_x86_64.whl 

EXPOSE 22 6006
CMD ["/usr/sbin/sshd", "-D"]

