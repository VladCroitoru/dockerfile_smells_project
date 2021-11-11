FROM ubuntu:18.04
ADD https://download.foldingathome.org/releases/public/release/fahclient/debian-stable-64bit/v7.5/fahclient_7.5.1_amd64.deb fahclient_7.5.1_amd64.deb
RUN dpkg -x fahclient_7.5.1_amd64.deb /tmp
CMD /tmp/usr/bin/FAHClient --fold-anon=true --log=/dev/null

