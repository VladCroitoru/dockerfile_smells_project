FROM tianon/debian:jessie

RUN uname -a && apt-get update --quiet && apt-get install --quiet --yes netselect-apt
RUN cd /etc/apt && netselect-apt && apt-get update
RUN apt-get install --quiet --yes curl && curl -L https://dl.google.com/go/go1.12.6.linux-amd64.tar.gz | tar xz -C /usr/local
RUN apt-get install --quiet --yes libgtk-3-dev
RUN apt-get install --quiet --yes build-essential
RUN apt-get install --quiet --yes git
RUN apt-get install --quiet --yes upx-ucl
RUN apt-get upgrade --quiet --yes
