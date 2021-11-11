FROM alpine:latest
MAINTAINER Nick Lang <nick@nicklang.com>

RUN apk add --update \
  python python-dev py-pip vim bash openssh git php php-mcrypt php-dev php-curl php-cli php-json php-apcu \
  && rm -rf /var/cache/apk/*

RUN git clone https://github.com/phacility/libphutil.git /opt/libphutil
RUN git clone https://github.com/phacility/arcanist.git /opt/arcanist

ENV PATH /opt/arcanist/bin/:$PATH
ENV HOME /home/root

RUN pip install pep8

# RUN source /opt/arcanist/resources/shell/bash-completion
VOLUME ["/data", "/arcanist", "/git", "/ssh"]
WORKDIR "/data"
RUN mkdir -p /home/root
RUN mkdir -p /git/gitconfig
RUN ln -s /git/gitconfig /home/root/.gitconfig
RUN ln -s /ssh/ /home/root/.ssh


ENTRYPOINT ["/opt/arcanist/bin/arc", "--arcrc-file=/arcanist/arcrc"]
CMD ["help"]
