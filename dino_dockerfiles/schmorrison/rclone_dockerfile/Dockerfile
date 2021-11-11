##docker run --name rclone -it --rm -v $PWD/.rclone.conf:/root/.rclone.conf schmorrison/rclone_dockerfile sh -c "rclone -v copy /source/ [remote]:/dest/"

FROM debian:jessie

MAINTAINER schmorrison

WORKDIR  /root/

RUN apt-get update && \
	apt-get -y install wget unzip less && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget http://pub.rclone.org/v1.29-33-g085677d%CE%B2/rclone-v1.29-33-g085677d%CE%B2-linux-amd64.zip && \
	  unzip rclone-v1.29-33-g085677d??-linux-amd64.zip && \
	  rm rclone-v1.29-33-g085677d??-linux-amd64.zip && \
	  mv  rclone-v1.29-33-g085677d#U03b2-linux-amd64/rclone /usr/bin/ && \
	  rm -rf rclone-*