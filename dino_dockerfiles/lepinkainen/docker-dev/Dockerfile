FROM ubuntu:rolling as lepinkainen-dev

RUN apt-get update && apt-get install -y locales  \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN apt-get install -y git build-essential python3 python3-pip curl wget

WORKDIR /tmp/
RUN curl -sL https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz --output golang_latest.tar.gz \
        && tar -C /usr/local -xzf golang_latest.tar.gz && rm golang_latest.tar.gz

ENV PATH "$PATH:/usr/local/go/bin"

# Common go packages
RUN go get -u github.com/golang/dep/cmd/dep \
              github.com/sirupsen/logrus

# Common python packages
RUN pip3 install requests

RUN mkdir /project
WORKDIR /project
VOLUME /project


#RUN rm -rf /var/lib/apt/lists/*