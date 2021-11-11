FROM docker

MAINTAINER Zeyu Ye <Shuliyey@gmail.com>

RUN apk add --update curl

RUN curl -sL https://releases.rancher.com/dapper/latest/dapper-`uname -s`-`uname -m` > /usr/local/bin/dapper \
  && chmod +x /usr/local/bin/dapper \
  && echo "ipv6" >> /etc/modules

RUN rm -rf ~/* \
  && rm -rf /var/cache/apk/* \

ENTRYPOINT []

CMD ["ash"]
