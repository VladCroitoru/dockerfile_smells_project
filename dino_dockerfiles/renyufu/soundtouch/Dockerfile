FROM renyufu/ubuntubase
RUN wget http://www.surina.net/soundtouch/soundtouch-1.9.2.tar.gz
RUN tar -xvf soundtouch-1.9.2.tar.gz
WORKDIR /soundtouch
RUN ./bootstrap && ./configure && make && make install
RUN ldconfig
VOLUME /dir
WORKDIR /dir
ENTRYPOINT ["soundstretch"]
