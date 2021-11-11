FROM ubuntu:14.04
RUN apt-get update; apt-get install -y xfce4 tightvncserver git autoconf automake libtool g++ libgsl0-dev python-numpy python-ply python-gtk2-dev libboost-dev libboost-python-dev libgtkmm-2.4-dev libgtkglextmm-x11-1.2-dev libhdf5-dev openssh-server valgrind; git clone git://github.com/ecell/spatiocyte; cd /spatiocyte; ./autogen.sh; ./configure; make; make install
RUN mkdir ~/.vnc; touch ~/.vnc/passwd; echo password | vncpasswd -f > ~/.vnc/passwd; chmod 600 ~/.vnc/passwd
RUN cd; echo "export LD_LIBRARY_PATH=/usr/local/lib" >> .bashrc
EXPOSE 5901
#CMD USER=root vncserver :1 -geometry 1360x768 -depth 24
