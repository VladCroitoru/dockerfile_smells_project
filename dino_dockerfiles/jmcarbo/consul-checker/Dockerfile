FROM ubuntu
# Mercurial
RUN echo 'deb http://ppa.launchpad.net/mercurial-ppa/releases/ubuntu precise main' > /etc/apt/sources.list.d/mercurial.list
RUN echo 'deb-src http://ppa.launchpad.net/mercurial-ppa/releases/ubuntu precise main' >> /etc/apt/sources.list.d/mercurial.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 323293EE

RUN apt-get update
RUN apt-get install -y curl git bzr mercurial unzip wget mysql-client

ADD https://dl.bintray.com/mitchellh/consul/0.4.1_linux_amd64.zip /tmp/consul.zip
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm /tmp/consul.zip

RUN curl -s https://storage.googleapis.com/golang/go1.3.3.linux-amd64.tar.gz | tar -v -C /usr/local/ -xz

ENV PATH /usr/local/go/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin
ENV GOPATH /go
ENV GOROOT /usr/local/go

#RUN go get github.com/jmcarbo/consul-alerts
#WORKDIR /go/src/github.com/jmcarbo/consul-alerts
#ADD . /go/src/github.com/jmcarbo/consul-alerts
#RUN go get
#RUN go build

ADD start /usr/local/bin/start
RUN chmod +x /usr/local/bin/start

EXPOSE 9000

ENTRYPOINT [   ]
CMD [ ]
