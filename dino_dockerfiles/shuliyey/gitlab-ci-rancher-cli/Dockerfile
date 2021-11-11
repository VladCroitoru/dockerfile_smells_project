FROM docker

MAINTAINER Zeyu Ye <Shuliyey@gmail.com>

ADD https://github.com/rancher/cli/releases/download/v0.6.1-rc1/rancher-linux-amd64-v0.6.1-rc1.tar.gz /

RUN cd / \
  && tar zxvf rancher-linux-amd64-v0.6.1-rc1.tar.gz \
  && mv rancher-v0.6.1-rc1/rancher /usr/bin/rancher \
  && echo "ipv6" >> /etc/modules

RUN apk add --update \
  py-pip jq

RUN pip install --upgrade pip \
  && pip install j2cli[yaml]

RUN rm -rf ~/* \
  && rm -rf /var/cache/apk/* \
  && rm -rf /rancher-linux-amd64-v0.6.1-rc1.tar.gz /rancher-v0.6.1-rc1

ENTRYPOINT []

CMD ["ash"]
