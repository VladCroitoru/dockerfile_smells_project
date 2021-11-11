FROM debian:jessie

ADD ./install_go.sh /install_go.sh

RUN chmod 0755 /install_go.sh
RUN adduser --uid 999 builder

RUN apt-get -qq update
RUN apt-get -qq install curl git libreadline-dev build-essential

RUN /usr/sbin/adduser --system --uid 999 builder --disabled-password --no-create-home
RUN /install_go.sh

ENV GOROOT /go
ENV GOPATH /workspace
ENV PATH /sbin:/usr/sbin:/bin:/usr/bin:/go/bin:/workspace/bin

