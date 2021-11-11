FROM sequenceiq/pam
MAINTAINER Gerencio

RUN yum -y update &  yum install -y unzip curl && curl -Lso /tmp/serf.zip https://releases.hashicorp.com/serf/0.7.0/serf_0.7.0_linux_amd64.zip && mkdir -p /usr/local/serf/bin && unzip /tmp/serf.zip -d /usr/local/serf/bin && ln -s /usr/local/serf/bin/serf /usr/local/bin/serf && rm /tmp/serf.zip
ENV SERF_HOME /usr/local/serf
ADD serf $SERF_HOME

#RUN mkdir -p /usr/local/init
ADD init /usr/local/init

EXPOSE 7373 7946
CMD /usr/local/serf/bin/start-serf-agent.sh
