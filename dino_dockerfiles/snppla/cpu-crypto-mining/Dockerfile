from ubuntu

RUN apt-get update &&  apt-get install -y build-essential libcurl4-openssl-dev git automake libtool libjansson* libncurses5-dev libssl-dev
RUN git clone --recursive https://github.com/tpruvot/cpuminer-multi.git -b linux
WORKDIR /cpuminer-multi

RUN ./autogen.sh
RUN ./configure CFLAGS="-march=native" --with-crypto --with-curl
RUN make

CMD nice -n 20 ./cpuminer -a cryptonight --url="stratum+tcp://cryptonight.usa.nicehash.com:3355" --userpass="3E1tMoSq6XJusnZ1k52rKm3dRanvyTMR4y:x" 
