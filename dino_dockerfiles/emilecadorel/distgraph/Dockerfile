FROM ubuntu:16.04

RUN apt-get -y update && \
     apt-get -y install sudo pkg-config git build-essential \
     software-properties-common aspcud unzip curl wget && \     
     wget http://master.dl.sourceforge.net/project/d-apt/files/d-apt.list -O /etc/apt/sources.list.d/d-apt.list && \
     apt-get update && apt-get -y --allow-unauthenticated install --reinstall d-apt-keyring && \
     add-apt-repository ppa:kedazo/libssh-0.7.x && \
     apt-get update && \
     apt-get -y install dmd-bin dub emacs libssh-dev 
          

RUN useradd -ms /bin/bash dist && echo "dist:dist" | chpasswd && adduser dist sudo
USER dist
WORKDIR /home/dist
RUN git clone --depth=1 https://github.com/EmileCadorel/distGraph.git

WORKDIR  /home/dist/distGraph

RUN /bin/bash /home/dist/distGraph/configure.sh

WORKDIR  /home/dist

# overwrite this with 'CMD []' in a dependent Dockerfile
CMD ["/bin/bash"]
