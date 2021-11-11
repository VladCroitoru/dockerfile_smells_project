FROM dockerfile/ubuntu
FROM dockerfile/java:oracle-java8
MAINTAINER Bradley Davis <bradley.davis@unc.edu>

ENV ACTIVATOR_VERSION 1.2.10
ENV PATH $PATH:/tmp/activator-$ACTIVATOR_VERSION

WORKDIR /tmp

ADD http://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip /tmp/activator.zip
#ADD /activator.zip /tmp/activator.zip
RUN unzip /tmp/activator.zip

ADD https://github.com/oasisclinic/surveyr/archive/master.zip /tmp/master.zip
RUN unzip /tmp/master.zip

EXPOSE 9000

WORKDIR /tmp/surveyr-master

RUN ["activator", "clean", "stage"]

RUN mkdir /app
RUN mv /tmp/surveyr-master/target/universal/stage/ /app/
RUN rm -rf /tmp

WORKDIR /app/stage
ENTRYPOINT ["/app/stage/bin/oasis-surveyr", "-Dapplication.domain=http://54.173.152.217 -Dapplication.secret=or7_xe;JHTm4@OS`cjh/PM4=7okeqi8h^Bba0_;NiPJSvijKH^:Q>03Qygq^`W9V"]