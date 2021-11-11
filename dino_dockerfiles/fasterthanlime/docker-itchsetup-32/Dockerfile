FROM 32bit/debian:latest

RUN uname -a && apt-get update --quiet && apt-get install --quiet --yes netselect-apt
RUN cd /etc/apt && netselect-apt && apt-get update
RUN apt-get install --quiet --yes curl && curl -L https://storage.googleapis.com/golang/go1.10.1.linux-386.tar.gz | tar xz -C /usr/local
RUN apt-get install --quiet --yes libgtk-3-dev
RUN apt-get install --quiet --yes build-essential
RUN apt-get install --quiet --yes rsync
RUN apt-get install --quiet --yes git
RUN apt-get install --quiet --yes upx-ucl
