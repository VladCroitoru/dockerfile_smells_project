FROM ubuntu:16.04

RUN DEBIAN_FRONTEND=noninteractive; apt-get update && \
	apt-get install -y software-properties-common python-software-properties

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | \
  	 debconf-set-selections

RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | \
  	 debconf-set-selections

RUN DEBIAN_FRONTEND=noninteractive; add-apt-repository ppa:webupd8team/java && \
	apt-get update && \
	apt-get install -y firefox sudo oracle-java8-installer


# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer

CMD ["/usr/bin/firefox"]
