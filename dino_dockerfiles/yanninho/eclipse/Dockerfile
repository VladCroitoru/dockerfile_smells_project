FROM  ubuntu:14.04 
MAINTAINER Yannick Saint Martino

# make sure the package repository is up to date
RUN apt-get update -y && apt-get install -y wget openjdk-7-jdk && rm -rf /var/lib/apt/lists/*

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/eclipseuser && \
    echo "eclipseuser:x:${uid}:${gid}:Developer,,,:/home/eclipseuser:/bin/bash" >> /etc/passwd && \
    echo "eclipseuser:x:${uid}:" >> /etc/group && \
    echo "eclipseuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/eclipseuser && \
    chmod 0440 /etc/sudoers.d/eclipseuser && \ 
    chown ${uid}:${gid} -R /home/eclipseuser

RUN cd  ~ && \
        wget http://ftp-stud.fht-esslingen.de/pub/Mirrors/eclipse/technology/epp/downloads/release/luna/R/eclipse-jee-luna-R-linux-gtk-x86_64.tar.gz && \
        tar -xzvf eclipse-jee-luna-R-linux-gtk-x86_64.tar.gz && \
        rm eclipse-jee-luna-R-linux-gtk-x86_64.tar.gz && \
	mv eclipse /opt/	
	
RUN mkdir -p /home/eclipseuser/workspace
RUN chown eclipseuser:eclipseuser -R /home/eclipseuser && chown eclipseuser:eclipseuser -R /opt/eclipse

USER eclipseuser
ENV HOME /home/eclipseuser
ENV PATH /home/eclipseuser/eclipse:$PATH

#WORKDIR /home/eclipseuser

VOLUME ["/home/eclipseuser/workspace"]

CMD /opt/eclipse/eclipse

#CMD /usr/sbin/sshd -D

