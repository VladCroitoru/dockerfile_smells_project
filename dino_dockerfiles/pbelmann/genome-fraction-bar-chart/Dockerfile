FROM ubuntu:16.04

ADD .Rprofile /project/

WORKDIR /project

ADD packrat /project/packrat

ADD install.sh /

RUN /install.sh && rm /install.sh

ADD bar_chart.r /project
ADD biobox.yaml /project
