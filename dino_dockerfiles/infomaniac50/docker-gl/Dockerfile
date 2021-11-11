# Base docker image
FROM ubuntu:trusty
MAINTAINER Derek Chafin <infomaniac50@gmail.com>

# Install all the things
RUN apt-get update && apt-get -y upgrade && \
    # Install GLXGears
    apt-get install -y mesa-utils && \
    apt-get install -y mesa-utils-extra

# Install all the things
# RUN apt-get update && apt-get -y upgrade
#     # Install GLXGears
# RUN apt-get install -y mesa-utils
# RUN apt-get install -y mesa-utils-extra

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    gpasswd -a developer video && \
    cp /etc/skel/.bash_logout /home/developer && \
    cp /etc/skel/.bashrc /home/developer && \
    cp /etc/skel/.profile /home/developer && \
    chown ${uid}:${gid} -R /home/developer

ENV LIBGL_DEBUG verbose

CMD ["glxgears"]