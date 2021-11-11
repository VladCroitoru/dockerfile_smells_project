FROM openmicroscopy/octave:latest
MAINTAINER markta31@gmail.com

USER root
WORKDIR /root
RUN apt-get update && apt-get -y install openssh-server less octave-info
RUN mkdir /var/run/sshd
RUN echo "octave:octave" | chpasswd
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22

USER octave
WORKDIR /home/octave
VOLUME ["/source"]
ENTRYPOINT ["octave"]

