FROM circleci/node:latest

RUN sudo apt-get update

# aws-cli install
RUN sudo apt-get update -qq && sudo apt-get install -y postgresql python-pip python-dev build-essential
RUN sudo pip install --upgrade pip
RUN sudo pip install --upgrade virtualenv
RUN sudo pip install awscli
RUN aws --version

# firebase install
RUN sudo npm install -g firebase-tools
