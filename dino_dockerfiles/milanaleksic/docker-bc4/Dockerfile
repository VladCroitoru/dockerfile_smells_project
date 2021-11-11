FROM debian:8.5

RUN apt-get update && \
	apt-get upgrade -y && \	
	apt-get install wget libqt4-opengl libqtgui4 libqtcore4 libqtwebkit4 poppler-utils -y && \
	mkdir -p /opt/beyond_compare_4/

RUN	wget http://www.scootersoftware.com/bcompare-4.1.9.21719_amd64.deb -O /opt/beyond_compare_4/bcompare.deb

RUN	dpkg -i /opt/beyond_compare_4/bcompare.deb

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    mkdir -p /etc/sudoers.d/ && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

VOLUME /media/milan/

USER developer
ENV HOME /home/developer
CMD /usr/bin/bcompare
