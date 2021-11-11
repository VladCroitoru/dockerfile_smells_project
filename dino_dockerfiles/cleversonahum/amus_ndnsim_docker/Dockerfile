FROM ubuntu:14.04
MAINTAINER Cleverson Nahum <cleversonahum@gmail.com>

#install pre-requesits for ndn-cxx, ns-3, etc...
RUN apt update
RUN apt-get install -y git
RUN apt-get install -y python-dev python-pygraphviz python-kiwi
RUN apt-get install -y python-pygoocanvas python-gnome2
RUN apt-get install -y python-rsvg ipython
RUN apt-get install -y build-essential
RUN apt-get install -y libsqlite3-dev libcrypto++-dev
RUN apt-get install -y libboost-all-dev


# install pre-requesits for libdash
RUN apt-get install -y git-core cmake libxml2-dev libcurl4-openssl-dev

# install mercurial for BRITE
RUN apt-get install -y mercurial

#Set Directory
RUN mkdir /home/ndnSIM
WORKDIR /home/ndnSIM/

#Brite
RUN hg clone http://code.nsnam.org/BRITE
RUN cd BRITE && make
RUN cd BRITE && sudo cp libbrite.so /usr/lib/

#Libdash
RUN git clone https://github.com/bitmovin/libdash.git
RUN cd libdash/libdash && mkdir build
RUN cd libdash/libdash/build && cmake ../
RUN cd libdash/libdash/build && make dash
RUN sudo cp ./libdash/libdash/build/bin/libdash.so  /usr/local/lib/
RUN sudo mkdir /usr/local/include/libdash
RUN sudo cp -r ./libdash/libdash/libdash/include/* /usr/local/include/libdash/

#Cloning ndn-cxx, amus-ndnSIM, itec-ndn and checkout to recommended versions
RUN git clone https://github.com/named-data/ndn-cxx.git ndn-cxx
RUN git clone https://github.com/cawka/ns-3-dev-ndnSIM.git ns-3
RUN git clone https://github.com/cawka/pybindgen.git pybindgen
RUN git clone https://github.com/ChristianKreuzberger/amus-ndnSIM.git ns-3/src/ndnSIM
RUN git clone https://github.com/danposch/itec-ndn.git
RUN cd pybindgen && git checkout e11c02d87924d92ee80991c9d663e1398a468008
RUN cd ndn-cxx && git checkout a1ffbc7a256f308d0ac318f02ebba1d6fa2305f8
RUN cd ns-3 && git checkout 4e388e47d715c3206374974a40cbab7ce428936f
RUN cd ns-3/src/ndnSIM/ git checkout 86a881d9898df74fa4cfd8e85684a3ae81ab02e6

#Paths to NDN forwarders
RUN cp itec-ndn/extern/forwarder.cpp ns-3/src/ndnSIM/NFD/daemon/fw/forwarder.cpp
RUN cp itec-ndn/extern/forwarder.hpp ns-3/src/ndnSIM/NFD/daemon/fw/forwarder.hpp
RUN cp itec-ndn/extern/ndn-content-store.hpp ns-3/src/ndnSIM/model/cs/ndn-content-store.hpp
RUN cp itec-ndn/extern/content-store-impl.hpp ns-3/src/ndnSIM/model/cs/content-store-impl.hpp
RUN cp itec-ndn/extern/content-store-nocache.hpp ns-3/src/ndnSIM/model/cs/content-store-nocache.hpp
RUN cp itec-ndn/extern/content-store-nocache.cpp ns-3/src/ndnSIM/model/cs/content-store-nocache.cpp
RUN cp itec-ndn/extern/strategy.cpp ns-3/src/ndnSIM/NFD/daemon/fw/strategy.cpp
RUN cp itec-ndn/extern/strategy.hpp ns-3/src/ndnSIM/NFD/daemon/fw/strategy.hpp

#install ndn-cxx
RUN cd ndn-cxx && ./waf configure
RUN cd ndn-cxx && ./waf
RUN cd ndn-cxx && sudo ./waf install

#install ns-3 with amus and Brite
RUN cd ns-3 && ./waf configure -d optimized --with-brite=../BRITE
RUN cd ns-3 && ./waf
RUN cd ns-3 && sudo ./waf install
RUN cd ns-3/build && sudo cp ./libns3-dev-brite-optimized.so /usr/local/lib/
RUN cd BRITE && sudo cp *.h /usr/local/include/ns3-dev/ns3
RUN cd BRITE && sudo mkdir /usr/local/include/ns3-dev/ns3/Models
RUN cd BRITE/Models && sudo cp *.h /usr/local/include/ns3-dev/ns3/Models

#itec-ndn scenario
RUN sudo ln -s lib/x86_64-linux-gnu/ /usr/lib64
RUN cd itec-ndn && ./waf configure
RUN cd itec-ndn && ./waf
RUN cd itec-ndn && sudo ./waf install

#Download MPEG DASH dataset
#RUN apt-get install -y wget
#RUN wget -c -r ftp://ftp-itec.aau.at/pub/icn/ccr_dataset/