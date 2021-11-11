FROM ubuntu:trusty
MAINTAINER hmxrobert

RUN echo "Asia/Tokyo\n" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get -y install software-properties-common && \
    add-apt-repository ppa:mc3man/trusty-media && \
    apt-get update && apt-get install -y \
        ntp \
        curl \
        libav-tools \
        rtmpdump \
        swftools \
        git \
        ffmpeg

# http://blog.gopheracademy.com/advent-2014/easy-deployment/
RUN mkdir /goroot && curl https://storage.googleapis.com/golang/go1.7.1.linux-amd64.tar.gz | tar xvzf - -C /goroot --strip-components=1

ENV GOROOT /goroot
ENV GOPATH /gopath
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin

RUN go get -d gopkg.in/robfig/cron.v2 && go get -v github.com/hmxrobert/radicast

ENTRYPOINT ["radicast"]
CMD ["--help"]
