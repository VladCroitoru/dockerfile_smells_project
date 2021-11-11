FROM ubuntu:14.04

ENV QT_X11_NO_MITSHM=1

RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN apt-get update
#RUN apt-get install -y python-software-properties
RUN apt-add-repository "deb http://apt.isis.rl.ac.uk trusty main"
RUN apt-add-repository ppa:mantid/mantid
RUN apt-get update
RUN apt-get install -y --force-yes mantid

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/docker_gui && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/docker_gui:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/docker_gui && \
    chmod 0440 /etc/sudoers.d/docker_gui && \
    chown ${uid}:${gid} -R /home/docker_gui

USER developer
ENV HOME /home/docker_gui
CMD /opt/Mantid/bin/MantidPlot
