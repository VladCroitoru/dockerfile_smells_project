FROM jenkins/jenkins:lts

# Use root to be able to install packages
USER root

# Install packages to allow apt to use a repository over HTTPS
RUN apt-get update && apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

# Add Docker’s official GPG key
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add -

# Add the Docker repository
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable"

# Update the apt package index
RUN apt-get update

# Install Docker CE
RUN apt-get install -y docker-ce