FROM       ubuntu:yakkety
MAINTAINER Florian Klink <flokli@flokli.de>

RUN apt-get update && apt-get install -y dirmngr apt-transport-https
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 11E9DE8848F2B65222AA75B8D1820DB22A11534E
RUN bash -c "echo 'deb https://weechat.org/ubuntu yakkety main' >/etc/apt/sources.list.d/weechat.list"
RUN bash -c "echo 'deb-src https://weechat.org/ubuntu yakkety main' >>/etc/apt/sources.list.d/weechat.list"

RUN apt-get update && apt-get install -y \
  weechat weechat-plugins weechat-scripts \
  python-pip python-potr \
  bitlbee-libpurple bitlbee-plugin-otr \
  rxvt-unicode-256color

RUN locale-gen en_US.UTF-8
RUN locale-gen de_DE.UTF-8
RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime

ADD bitlbee.conf /etc/bitlbee/bitlbee.conf

RUN pip install websocket-client

ADD run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]
