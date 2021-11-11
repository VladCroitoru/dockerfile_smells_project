FROM ubuntu:16.04
MAINTAINER Atis Gūtmanis

RUN apt-get update && apt-get upgrade -yqq && apt-get install -yqq python3 python3-pip curl php git openssl curl php-curl

WORKDIR /root

RUN git clone https://github.com/lukas2511/dehydrated \
  && git clone https://github.com/josteink/le-godaddy-dns \
  && git clone https://github.com/N1ghteyes/cpanel-UAPI-php-class cpanel \
  && python3 -m pip install --upgrade pip \
  && python3 -m pip install -r le-godaddy-dns/requirements.txt --user

ADD job.sh /root/
ADD ssldeploy.php /root/
RUN chmod u+x /root/job.sh
