FROM ubuntu:zesty
MAINTAINER George Liu <https://github.com/centminmod/docker-ubuntu-cpuminer>
# https://moneropool.com/#getting_started
# update-alternatives --config gcc
# update-alternatives --config ld
ENV GIT_URL https://github.com/wolf9466/cpuminer-multi.git
ENV POOL_URL mine.moneropool.com:3333
ARG DEBIAN_FRONTEND=noninteractive
COPY threads.sh /threads.sh
RUN . /threads.sh && /bin/echo $THREADS
ENV THREADS=$THREADS
RUN ulimit -c -m -s -t unlimited && apt-get update && apt-get -y install nano dirmngr wget apt-utils libcurl3 build-essential libjansson-dev git make automake bc libcurl4-openssl-dev && touch /etc/apt/sources.list.d/gcc7.list && echo "deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu zesty main " >> /etc/apt/sources.list.d/gcc7.list && echo "deb-src http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu zesty main " >> /etc/apt/sources.list.d/gcc7.list && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 60C317803A41BA51845E371A1E9377A2BA9EF27F && apt-get update && apt-get -y install gcc-4.8 g++-4.8 gcc-4.9 g++-4.9 gcc-5 g++-5 gcc-7 g++-7 ; update-alternatives --remove-all gcc ; update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 30 --slave /usr/bin/g++ g++ /usr/bin/g++-4.8 ; update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 40 --slave /usr/bin/g++ g++ /usr/bin/g++-4.9 ; update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 50 --slave /usr/bin/g++ g++ /usr/bin/g++-5 ; update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave /usr/bin/g++ g++ /usr/bin/g++-6 ; update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 70 --slave /usr/bin/g++ g++ /usr/bin/g++-7 ; update-alternatives --set gcc "/usr/bin/gcc-7"; update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.gold" 20; update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.bfd" 10; update-alternatives --set ld "/usr/bin/ld.gold"
RUN git clone ${GIT_URL} cpuminer && cd cpuminer && ./autogen.sh -m4_pattern_allow && ./configure && make -j"$(/bin/grep -c "processor" /proc/cpuinfo)" && apt-get autoclean && apt-get remove && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ;
RUN /bin/bash -l -c "/bin/echo $THREADS"

WORKDIR /cpuminer
ENTRYPOINT  ["./minerd","-a","cryptonight","-o","stratum+tcp://mine.moneropool.com:3333","-p","x"]
CMD ["-u","$WALLETADDR","-t","$THREADS"]

