FROM renyufu/ubuntubase
RUN wget http://jaist.dl.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz
RUN tar -xvf lame-3.99.5.tar.gz
WORKDIR /lame-3.99.5
RUN ./configure && make && make install
RUN ldconfig
VOLUME /mp3
WORKDIR /mp3
ENTRYPOINT ["lame"]
