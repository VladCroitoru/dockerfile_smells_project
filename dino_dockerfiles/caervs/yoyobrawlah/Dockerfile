FROM ubuntu:12.04
MAINTAINER pdevine
RUN apt-get update && apt-get install -y python-pip
RUN apt-get install -y freeglut3 libglu1 libfreetype6 libfreetype6 libavbin0 libopenal1
#RUN apt-get install -y libav-utils
RUN apt-get install -y fontconfig
RUN pip install pyglet

# This is for ubuntu 14.04, however pyglet and avbin don't work well together in 14.04
#RUN export uid=1000 gid=1000 && \
#    mkdir -p /home/developer && \
#    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
#    echo "developer:x:${uid}:" >> /etc/group && \
#    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
#    chmod 0440 /etc/sudoers.d/developer && \
#    chown ${uid}:${gid} -R /home/developer

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/developer

COPY run_game.py yoyo/run_game.py
COPY data/* yoyo/data/
COPY gamelib/*.py yoyo/gamelib/

USER developer
ENV HOME /home/developer

CMD cd /yoyo && python run_game.py

# This is a new Dockerfile line