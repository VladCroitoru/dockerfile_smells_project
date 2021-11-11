FROM debian:8
# cause of https://bugzilla.redhat.com/show_bug.cgi?id=1404290 prevents build of socat2 branch on debian:latest

RUN apt-get update && apt-get install -y gcc make autoconf libssl-dev git

RUN git clone git://repo.or.cz/socat.git /src

RUN cd /src && git checkout origin/socat2 && \
   autoconf && ./configure && make -j24 progs && \
   touch doc/socat.1 && touch doc/socat.html && \
   make install && \
   cd / && rm -rf /src

CMD ["socat"]
