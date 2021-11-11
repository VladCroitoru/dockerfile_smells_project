FROM navicore/naviron-gambit

MAINTAINER Ed Sweeney <ed@onextent.com>

WORKDIR /opt

RUN git clone https://github.com/vyzo/gerbil.git && cd gerbil/src && PATH=$PATH:/opt/gambit/v4.8.8/bin ./build.sh

