FROM  ubuntu
MAINTAINER Tom Robinson <tomjrob@modhub.io>

RUN apt-get update && apt-get install curl git build-essential patch openssh-client ruby-dev zlib1g-dev liblzma-dev -y
RUN curl -L https://www.opscode.com/chef/install.sh | sudo bash -s -- -P chefdk
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
