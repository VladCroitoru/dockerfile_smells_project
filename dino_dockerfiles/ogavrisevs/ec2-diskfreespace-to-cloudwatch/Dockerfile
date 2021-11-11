FROM alpine:latest

MAINTAINER Oskars.G <no_spam_here@me.me>

RUN apk add --no-cache --upgrade coreutils && \
  apk add --no-cache curl unzip && \
  apk add --no-cache perl perl-switch perl-datetime perl-unix-syslog perl-lwp-protocol-https perl-digest-sha1

ENV CWMS_VERSION=CloudWatchMonitoringScripts-1.2.1.zip

RUN curl http://aws-cloudwatch.s3.amazonaws.com/downloads/${CWMS_VERSION} -O -s

RUN unzip CloudWatchMonitoringScripts-1.2.1.zip

WORKDIR aws-scripts-mon

ENTRYPOINT ["/aws-scripts-mon/mon-put-instance-data.pl", "--disk-space-util", "--disk-path=/host_root"]
