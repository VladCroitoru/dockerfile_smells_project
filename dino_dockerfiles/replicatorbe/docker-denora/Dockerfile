FROM debian:jessie
MAINTAINER Jérôme Fafchamps (sMug [replicatorbe]) <smug@smug.fr>
RUN apt-get update && \
    apt-get upgrade -y && \ 
    apt-get install -y build-essential libmysqlclient-dev zip unzip gcc wget && \
    apt-get clean 

RUN useradd -ms /bin/bash denora
USER denora
WORKDIR /home/denora

RUN wget "http://downloads.sourceforge.net/project/denora/Denora%20Release/Denora%201.5.0/denora-1.5.0.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fdenora%2Ffiles%2FDenora%2520Release%2FDenora%25201.5.0%2Fdenora-1.5.0.tar.gz%2Fdownload&ts=1436694873&use_mirror=freefr" -O denora.tar.gz
RUN tar zxvf denora.tar.gz && \ 
cd denora && \
./configure --with-bindir=/home/denora/stats --with-datadir=/home/denora/stats --with-permissions=077 --enable-crypt --enable-mtrace  && \
make && \
make install 
COPY denora.conf /home/denora/stats/

CMD ["/home/denora/stats/stats", "-nofork"]
