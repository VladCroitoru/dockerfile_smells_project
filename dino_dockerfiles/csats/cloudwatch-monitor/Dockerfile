FROM ubuntu:14.04

RUN \
  apt-get update && \
  apt-get -y dist-upgrade && \
  apt-get -y autoremove --purge && \
  apt-get install -y libwww-perl libdatetime-perl wget unzip && \
  wget http://aws-cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.1.zip && \
  echo "98fb930930b147d0a9cbe0e9bee4eb9c3aee3259  CloudWatchMonitoringScripts-1.2.1.zip" > SHA1SUM && \
  sha1sum -c SHA1SUM && \
  unzip CloudWatchMonitoringScripts-1.2.1.zip && \
  apt-get remove -y wget unzip && \
  rm CloudWatchMonitoringScripts-1.2.1.zip && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD run-forever.sh /

WORKDIR /

CMD [ "./run-forever.sh" ]
