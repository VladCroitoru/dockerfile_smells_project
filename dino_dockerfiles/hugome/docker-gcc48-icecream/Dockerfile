FROM gcc:4.8

RUN useradd icecc
WORKDIR /home/icecc
RUN apt-get update
RUN apt-get install -y libcap-ng-dev liblzo2-dev git docbook2x
RUN git clone https://github.com/icecc/icecream.git
WORKDIR icecream
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
ENV PATH "/home/icecc/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
RUN touch /var/log/icecc.log
CMD iceccd -d -l /var/log/icecc.log && tail -f /var/log/icecc.log
EXPOSE 10245/tcp 8765/tcp 8766/tcp 8765/udp
