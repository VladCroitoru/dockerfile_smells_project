FROM ubuntu:16.04

RUN \
  apt-get update -qq && \
  apt-get install -y \
    git \
    libcairo-dev \
    libedit-dev \
    python2.7 \
    python-pip

RUN mkdir /opt/gitlab
ADD requirements.txt /opt/gitlab/
RUN pip install -U -r /opt/gitlab/requirements.txt

ADD trello_commit_to_card.py /opt/gitlab/
RUN ls -la /opt/gitlab
ENV PATH /opt/gitlab:$PATH

