FROM circleci/openjdk:8
MAINTAINER Matt Strenz <mstrenz@gmail.com>
USER root

ENV DISPLAY=:1.0
RUN apt-get update && apt-get install -y vim xvfb python3
RUN apt-get upgrade -y
RUN apt-get update -y
RUN apt-get install -y default-jre-headless python3-tk python3-pip python3-dev libxml2-dev libxslt-dev zlib1g-dev
RUN pip3 install --upgrade pip
RUN pip3 install lxml
RUN pip3 install psutil
RUN pip3 install bzt
RUN pip3 install --upgrade bzt

RUN rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/*

ENV url https://www.example.com/
ENV users 5
ENV length 60s

RUN mkdir /tmp/load
WORKDIR /tmp/load
ENV HOME /tmp/load

COPY quick_test.yml /tmp/load
COPY site_test.yml /tmp/load

VOLUME /results
RUN chmod a+w /results /tmp/load

RUN bzt quick_test.yml
RUN rm -r /tmp/load/*-*-*_*-*-*.*
#RUN chmod a+x .bzt/jmeter-taurus/bin/jmeter .bzt/jmeter-taurus/bin/jmeter-server .bzt/jmeter-taurus/bin/*.sh
#RUN ln -s .bzt/jmeter-taurus/bin/jmeter
#RUN ln -s .bzt/jmeter-taurus/bin/jmeter-server


CMD bzt \
    -o scenarios.load.requests="['${url}']" \
    -o modules.console.disable=true \
    -o execution.0.concurrency=${users} \
    -o execution.0.hold-for=${length} site_test.yml 
 
