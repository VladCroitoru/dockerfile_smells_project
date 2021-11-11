FROM java:8

# maintainer details
MAINTAINER CharanV "charan.cse@gmail.com"

# update packages and install maven
RUN  \
  export DEBIAN_FRONTEND=noninteractive && \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y vim wget curl git maven

#install docker
RUN  \
  apt-get update && \
  apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
  curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" && \
  apt-get update && \
  apt-get -y install docker-ce
  
# attach volumes
VOLUME /volume/git

# create working directory
RUN mkdir -p /local/git
WORKDIR /local/git

# run terminal
CMD ["/bin/bash"]
