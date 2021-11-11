FROM jenkinsci/ssh-slave

# Make sure the package repository is up to date.
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y git

RUN apt-get install -y maven
# Standard SSH port
EXPOSE 22
