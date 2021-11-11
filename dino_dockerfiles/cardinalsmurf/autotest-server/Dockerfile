FROM python:2.7
MAINTAINER robert buckley <rbuckley@marvell.com>
ENV REFRESHED_AT 2016-10-19

RUN apt-get update && apt-get install -y curl
RUN pip install django==1.5 MySQL-python south
RUN curl -OL https://raw.github.com/autotest/autotest/master/contrib/install-autotest-server.sh && chmod +x install-autotest-server.sh

RUN ./install-autotest-server.sh -d test0000 -u test0000
EXPOSE 80
