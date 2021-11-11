# Instructions and other stuff casually stolen from https://github.com/gridcoin/Gridcoin-Research.
# Specifically, the build instructions for the gridcoin research client for Ubuntu.

FROM ubuntu
MAINTAINER Vishakh Kumar <vishakhpradeepkumar@gmail.com>

#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get -y update 






ARG BOINC_DIR=/root/boinc_dir
ARG EMAIL=vishakhpradeepkumar@gmail.com

ARG RPCUSER=grokkingStuff                                          
ARG RPCPASSWORD=2YoXwdv9bkxM3kcS9S4KK3C9ngopEzM1DVe9PEuaxVPc 




# Installing Normal Dependencies. 
RUN apt-get -y install ntp \
                       git \
                       build-essential \
                       libssl-dev \
                       libdb-dev \
                       libdb++-dev \
                       libqrencode-dev \
                       libcurl4-openssl-dev \
                       curl \
                       libzip-dev \
                       libzip4 \
                       libboost-atomic-dev \
                       libboost-chrono-dev \
                       libboost-date-time-dev \
                       libboost-filesystem-dev \
                       libboost-program-options-dev \
                       libboost-serialization-dev \
                       libboost-system-dev \
                       libboost-thread-dev \
                       wget 




# Dependencies for Gridcoin Daemon.
RUN apt-get -y update                \
    && apt-get -y install ntp git build-essential libssl-dev libdb-dev libdb++-dev libboost-all-dev libqrencode-dev \
    && apt-get -y install qt-sdk qt4-default \
    && apt-get -y install libcurl3-dev \
    && apt-get -y install libzip-dev
    




# Build Gridcoin Daemon.
# We'll be cloning from the github repo and following directions from there.
# Just to be explicit, the directions were found at Gridcoin-Research/doc/build-unix.txt
RUN cd ~ \
    && git clone https://github.com/gridcoin/Gridcoin-Research \
    && cd ~/Gridcoin-Research/src \
    && mkdir obj \
    && chmod 755 leveldb/build_detect_platform  \
    && make -f makefile.unix USE_UPNP=-  \
    && strip gridcoinresearchd \ 
    && install -m 755 gridcoinresearchd /usr/bin/gridcoinresearchd \
	&& mkdir ~/.GridcoinResearch \
	&& cd ~/.GridcoinResearch 



# add information to gridcoinresearch.conf.
RUN echo 'addnode=node.gridcoin.us\nserver=1                  \n\
rpcuser=$RPCUSER                                              \n\    
rpcpassword=$RPCPASSWORD                                      \n\
email=$EMAIL                                                  \n\
boincdatadir=$BOINC_DIR                                       ' \
>> ~/.GridcoinResearch/gridcoinresearch.conf                    \
    $$ cd ~                                                     \
    && mkdir $BOINC_DIR                                         \
    && cd $BOINC_DIR                                            \
    && pwd




# Run gridcoin daemon
CMD ["gridcoinresearchd"]





# Dependencies for Qt5 GUI for Gridcoin.
RUN apt-get -y install qt5-default qt5-qmake qtbase5-dev-tools qttools5-dev-tools \
    build-essential libboost-dev libboost-system-dev \
    libboost-filesystem-dev libboost-program-options-dev libboost-thread-dev \
    libssl-dev libdb++-dev libminiupnpc-dev





# Build Qt5 GUI.
RUN cd ~/Gridcoin-Research \
    && qmake "USE_UPNP=1" "USE_QRCODE=1" \
    && make


# Make GUI an actual executable
RUN cd ~/Gridcoin-Research \
&& strip gridcoinresearch \
&& install -m 755 gridcoinresearch /usr/bin/gridcoinresearch 

# Download most blocks from a source quickly, unpack the zip file and delete it.
RUN cd root/.GridcoinResearch/  \
 && wget https://spideroak.com/share/N4YFAZLQOBSXEMDP/public/d%3A/Gridcoin.Tools/Share/snapshot.zip -O blockchain.zip \
 && apt-get -y install unzip \
 && unzip blockchain.zip \
 && rm blockchain.zip


# Entrypoint for the host to access the application through X server.
# This allows the GUI to appear on the host, in simpler words.
ENTRYPOINT [ "gridcoinresearch" ]




