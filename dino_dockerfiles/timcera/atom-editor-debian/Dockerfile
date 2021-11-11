FROM debian:jessie
MAINTAINER Tim Cera <tim@cerazone.net>

ENV VERSION v1.7.2

RUN apt-get update -y && \
    apt-get install -y \
        curl           \
        git            \
        gconf2         \
        gconf-service  \
        libgtk2.0-0    \
        libnotify4     \
        libxtst6       \
        libnss3        \
        python         \
        gvfs-bin       \
        xdg-utils      \
        make           \
        gcc            \
        g++            \
        pandoc
RUN apt-get install -y \
        julia
RUN apt-get clean
RUN curl -L https://github.com/atom/atom/releases/download/${VERSION}/atom-amd64.deb > /tmp/atom.deb
RUN dpkg -i /tmp/atom.deb
RUN rm -f /tmp/atom.deb

# Called when the Docker image is started in the container
ADD start.sh /start.sh
RUN chmod 0755 /start.sh

CMD /start.sh
