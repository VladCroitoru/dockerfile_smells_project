# acoustid-index
#
# VERSION               0.0.1

FROM debian:wheezy

RUN apt-get update
RUN apt-get install -y cmake wget unzip build-essential libqt4-dev
RUN cd /opt/ ; wget https://bitbucket.org/acoustid/acoustid-index/get/e5a34adc918f.zip ; unzip *.zip ; mv acoustid-acoustid-index-* acoustid-index ; rm *.zip ; cd /opt/acoustid-index ; cmake . ; make install ; rm -rf /opt/acoustid-index ; mkdir /opt/acoustid-index
EXPOSE 6080

VOLUME /opt/acoustid-index

CMD ["fpi-server", "-a", "0.0.0.0", "-d", "/opt/acoustid-index"]
