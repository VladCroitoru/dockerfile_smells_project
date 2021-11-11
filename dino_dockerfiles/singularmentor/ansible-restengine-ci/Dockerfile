FROM ruby:2.3.1
MAINTAINER ariel@singularmentor.com.ar

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "curl", "openssh-client", "git", "rsync", "python-pip", "python-dev", "-y"]
RUN ["pip", "install", "ansible"]
