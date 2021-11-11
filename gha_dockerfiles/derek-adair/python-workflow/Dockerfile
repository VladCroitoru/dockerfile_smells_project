# derekadair/python-workflow:base
FROM python:3.7-buster
MAINTAINER Derek Adair "d@derekadair.com"

RUN apt-get update && apt-get -y upgrade

# install virtualenv
RUN pip install --upgrade virtualenv pip && \
    mkdir /virtualenv &&  \
    virtualenv /virtualenv 

ENV PATH=/virtualenv/bin:$PATH

CMD ["python"]
