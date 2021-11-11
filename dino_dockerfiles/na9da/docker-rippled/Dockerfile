FROM ubuntu:16.04

RUN apt update
RUN apt upgrade -y

RUN apt-get install yum-utils alien -y
RUN rpm -Uvh https://mirrors.ripple.com/ripple-repo-el7.rpm
RUN yumdownloader --enablerepo=ripple-stable --releasever=el7 rippled
RUN rpm --import https://mirrors.ripple.com/rpm/RPM-GPG-KEY-ripple-release && rpm -K rippled*.rpm
RUN alien -i --scripts rippled*.rpm && rm rippled*.rpm

VOLUME ["/opt/ripple"]
EXPOSE 51235 5005


CMD ["/opt/ripple/bin/rippled", "--conf", "/opt/ripple/etc/rippled.cfg"]

