FROM ubuntu:14.04 

RUN gpg --keyserver keys.gnupg.net --recv A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89
RUN gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -

ADD tor.list /etc/apt/sources.list.d/tor.list
RUN apt-get update
RUN apt-get install -y tor deb.torproject.org-keyring

ADD torrc /etc/tor/torrc

EXPOSE 9050
CMD [ "tor"]
