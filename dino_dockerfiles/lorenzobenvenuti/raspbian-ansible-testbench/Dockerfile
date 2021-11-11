from resin/rpi-raspbian

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install -y openssh-server python
RUN mkdir /var/run/sshd
RUN adduser --home /home/pi pi
RUN adduser pi sudo
RUN echo 'pi:raspberry' | chpasswd

RUN [ "cross-build-end" ]

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
