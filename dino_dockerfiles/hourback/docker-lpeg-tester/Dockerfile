FROM	ubuntu:vivid	
MAINTAINER Ali Nabavi <github@alijnabavi.info>

LABEL Description="This is for running my own LPEG tester for Heka sandbox plug-in development."
RUN apt-get update
RUN apt-get install -y cmake libwt-dev gcc git
RUN apt-get install -y make
RUN apt-get install -y wget
RUN apt-get install -y clang

RUN git clone https://github.com/trink/lpeg_tester.git

RUN apt-get install -y libboost-program-options-dev libboost-random-dev libboost-test-dev

EXPOSE 8889

RUN cd lpeg_tester && mkdir release && cd release && cmake -DCMAKE_BUILD_TYPE=release .. && make && make install DESTDIR=install

WORKDIR /lpeg_tester/release/install/usr/local/lpeg_tester

CMD ["bash", "run.sh"]

