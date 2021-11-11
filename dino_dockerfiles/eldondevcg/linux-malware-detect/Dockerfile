FROM debian:jessie
RUN apt-get update
RUN apt-get install -y wget bsdmainutils
ADD . /maldet
WORKDIR /maldet/
RUN bash install.sh
ENV EDITOR /bin/cat
WORKDIR /sample
ENTRYPOINT /usr/local/sbin/maldet -f /sample/linux_malware_detect_list -e
