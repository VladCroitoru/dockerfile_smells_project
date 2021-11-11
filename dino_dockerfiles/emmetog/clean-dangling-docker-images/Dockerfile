FROM ubuntu:14.10

MAINTAINER Emmet O'Grady <emmet789@gmail.com>

RUN sudo apt-get update && sudo apt-get install -y \
        curl

# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ubuntu/ | sh

CMD docker rmi $(docker images --filter 'dangling=true' | awk '{print $3}')
