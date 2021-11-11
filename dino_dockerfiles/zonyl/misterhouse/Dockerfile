FROM phusion/baseimage
LABEL maintainer "Jason Sharpee <jason@sharpee.com>"

EXPOSE 8080
ENV mh_parms=/usr/src/misterhouse/local/mh.private.ini


RUN [ "apt-get", "-q", "update" ]
RUN [ "apt-get", "-qy", "--force-yes", "upgrade" ]
RUN [ "apt-get", "-qy", "--force-yes", "dist-upgrade" ]
RUN [ "apt-get", "install", "-qy", "--force-yes", \
      "perl", \
      "build-essential", \
      "libgd-gd2-perl", \
      "libswitch-perl", \
      "perl-tk", \
      "libwww-perl", \
      "libcgi-pm-perl", \
      "libaudio-mixer-perl", \
      "cpanminus", \
      "libexpat1-dev" ]
RUN [ "apt-get", "clean" ]
RUN [ "rm", "-rf", "/var/lib/apt/lists/*", "/tmp/*", "/var/tmp/*" ]
RUN [ "cpanm", "Amazon::SNS" ]

COPY . /usr/src/misterhouse
RUN mkdir /usr/src/misterhouse/local
VOLUME ['/usr/src/misterhouse/local']

WORKDIR /usr/src/misterhouse/bin
CMD [ "perl", "./mh" ]
