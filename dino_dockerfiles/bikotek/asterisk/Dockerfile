FROM debian

MAINTAINER Unai Bikotek

RUN apt-get update && apt-get install -y asterisk wget sendemail

RUN wget http://asterisk.hosting.lv/bin/codec_g729-ast130-gcc4-glibc-x86_64-core2.so && mv codec_g729-ast130-gcc4-glibc-x86_64-core2.so /usr/lib/asterisk/modules/g729.so && /etc/init.d/asterisk restart

EXPOSE 5060
EXPOSE 10000:20000

CMD ["asterisk","-f"]

