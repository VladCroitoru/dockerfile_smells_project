FROM ubuntu:14.04
MAINTAINER  Austin Godber <godber@uberhip.com>
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get install -y build-essential python-setuptools python-dev && \
  easy_install pip
RUN pip install rq-dashboard
EXPOSE 9181
CMD ["rq-dashboard"]
