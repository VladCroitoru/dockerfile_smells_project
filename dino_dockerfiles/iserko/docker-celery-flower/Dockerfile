# Flower
#
# VERSION 0.1

FROM ubuntu:trusty
MAINTAINER Igor Serko <igor.serko@gmail.com>

# update the package repository and install python pip
RUN apt-get -y update && apt-get -y install python-dev python-pip

# installing flower
RUN pip install flower

# Make sure we expose port 5555 so that we can connect to it
EXPOSE 5555

# Running flower
ENTRYPOINT ["flower", "--port=5555"]