FROM ubuntu:latest
MAINTAINER DTI UNIFESP SJC
RUN apt-get update && apt-get upgrade -y && apt-get install -y sudo xvfb x11vnc fluxbox supervisor
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/octave && \    
    echo "octave:x:${uid}:${gid}:Octave,,,:/home/octave:/bin/bash">>/etc/passwd && \
    echo "octave:x:${uid}:" >> /etc/group && \
    touch /etc/sudoers.d/octave && \
    echo "octave ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/octave && \
    chmod 0440 /etc/sudoers.d/octave && \
    chown ${uid}:${gid} -R /home/octave
RUN apt-get install -y octave && apt-get autoclean
ENV DISPLAY :0
USER octave
CMD /usr/bin/octave
