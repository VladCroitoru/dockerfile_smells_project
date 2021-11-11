FROM ubuntu:16.04
MAINTAINER František Dvořák <valtri@civ.zcu.cz>

RUN apt-get update \
&& apt-get install -y puppet \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
