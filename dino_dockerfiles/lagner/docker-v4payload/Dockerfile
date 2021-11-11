FROM lagner/docker-basement

USER root

RUN apt-get update && apt-get install -y \
 "^libxcb.*-dev"\
 *cryptopp*\
 build-essential g++-5 gcc-5 cpp-5 gdb ccache\
 gcc-multilib lib32z1 lib32stdc++6 lib32ncurses5\
 flex bison\
 binutils\
 git\
 gperf\
 icu-devtools\
 libasound2-dev\
 libatspi2.0-0\
 libbz2-dev\
 libcap-dev\
 libdbus-c++-dev\
 libedit-dev\
 libfontconfig1-dev\
 libgles2-mesa-dev\
 libglu1-mesa-dev\
 libgstreamer1.0-0\
 libicu-dev\
 libnss3-dev\
 libpci-dev\
 libpulse-dev\
 libsdl*dev\
 libssl-dev\
 libtool\
 libudev-dev\
 libx11-xcb-dev\
 libxcb1-dev\
 libxcomposite-dev\
 libxcursor-dev\
 libxdamage-dev\
 libxrandr-dev\
 libxrender-dev\
 libxslt-dev\
 libxtst-dev\
 meld\
 mesa-common-dev\
 ninja-build\
 openjdk-8*\
 openssl\
 python\
 python-configparser\
 python-dev\
 python-pip\
 python3\
 python3-pip\
 fabric\
 zip

RUN update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.gold" 20
RUN dpkg --add-architecture i386

RUN pip install --upgrade pip
RUN pip install virtualenv gitpython six requests asyncio autobahn

# was got from parent container
USER ${worker}

CMD ["/bin/bash"]
