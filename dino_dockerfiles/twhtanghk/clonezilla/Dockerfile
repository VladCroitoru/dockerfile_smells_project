FROM debian:jessie

RUN apt-get update \
&& apt-get install -y clonezilla dialog parted dosfstools bc squashfs-tools \
&& apt-get clean

CMD top -b -d 1000
