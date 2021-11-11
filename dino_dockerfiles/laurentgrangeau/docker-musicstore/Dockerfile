FROM microsoft/aspnet

RUN apt-get -qqy update && apt-get -qqy upgrade && apt-get -qqy install git

RUN git clone https://github.com/aspnet/MusicStore.git

EXPOSE 5004

ADD start.sh /

RUN chmod 0755 /start.sh

CMD ["/start.sh"]