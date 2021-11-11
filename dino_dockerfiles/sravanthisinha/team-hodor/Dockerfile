FROM ubuntu:14.04
RUN apt-get update 
RUN apt-get install -y emacs
RUN apt-get install -y curl
RUN apt-get install -y python
RUN sudo apt-get install -y python-pygame
RUN sudo apt-get install -y git

RUN curl https://gist.githubusercontent.com/SravanthiSinha/ae5561ef3d6d6ef9577187711bec3824/raw/72987d440285ba8b0210d68b89595bfadad154f0/mazerunner.py > mazerunner.py

RUN git clone https://github.com/SravanthiSinha/free_python_games.git

RUN curl https://gist.githubusercontent.com/SravanthiSinha/767d1d8a6115ee103651fcdfcd762356/raw/647f4aa2a029845dafbb232653e1e617d56f53d7/games.sh > games.sh

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0600 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer
