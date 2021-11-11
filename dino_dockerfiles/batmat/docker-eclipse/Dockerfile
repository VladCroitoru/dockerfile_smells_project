FROM ndeloof/java

# Heavily based on http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/

MAINTAINER Baptiste Mathus <batmat@batmat.net>

# TODO : variabilize those values
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

WORKDIR /home/developer
RUN curl http://eclipse.ialto.com/technology/epp/downloads/release/luna/SR1/eclipse-java-luna-SR1-linux-gtk-x86_64.tar.gz | tar -xvz

RUN sudo apt-get update
RUN sudo apt-get install libswt-gtk-3-java -y

CMD /home/developer/eclipse/eclipse
