FROM ubuntu
ENV VE_version="MarchandD_20151117_v01.02"
# Read under  http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/
RUN apt-get update && apt-get install -y firefox
# Local command 'id -a' to display your ids and replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer
USER developer
ENV HOME /home/developer
CMD /usr/bin/firefox
# Security failure, reserved only to test quickly...
# docker run -ti -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --name firefox11 YOUR_IMAGE_NAME