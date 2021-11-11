FROM ericfont/armv7hf-debian-qemu

RUN [ "cross-build-start" ]

RUN echo "deb http://http.debian.net/debian wheezy-backports main" >> /etc/apt/sources.list
RUN apt-get update #so can use wheezy-backports whihc containe Qt 5.3.2
RUN apt-get install apt-utils #I think aptitude should have this for configuring
RUN apt-get install wget make automake gcc-4.7 g++-4.7 git cmake alsa-base libsndfile1 libasound2-dev portaudio19-dev libsndfile1-dev zlib1g-dev libfreetype6-dev libfreetype6 lame libmp3lame-dev libssl-dev libdrm-dev libgl1-mesa-dev libpulse-dev 

# get qt5, including debug symbols!
RUN apt-get install qtbase5-dev qttools5-dev qttools5-dev-tools qtquick1-5-dev qtscript5-dev libqt5xmlpatterns5-dev libqt5svg5-dev libqt5webkit5-dev qtbase5-dbg qttools5-dbg qtquick1-5-dbg qtscript5-dbg

# need to be able to use https for github
RUN apt-get install ca-certificates
RUN git config --global http.sslVerify true

# get and build AppImageKit
#RUN wget https://github.com/probonopd/AppImageKit/archive/5.tar.gz
#RUN tar -xvzf 5.tar.gz
#RUN bash AppImageKit-5/build.sh

RUN [ "cross-build-end" ]  
