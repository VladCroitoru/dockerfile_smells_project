# Uses Circle's latest Node image as the base
FROM circleci/node:latest

# Update aptitude
RUN sudo apt-get update && \
    sudo apt-get -y upgrade

# Install Python, pip, and Docker
RUN sudo apt-get install -y \
        python \
        python-pip \
        python-dev \
        docker

# Install AWS CLI
RUN sudo pip install --upgrade awscli

# Install AWS SAM
RUN sudo wget -q https://github.com/awslabs/aws-sam-local/releases/download/v0.2.8/sam_0.2.8_linux_amd64.deb

RUN sudo dpkg -i sam_0.2.8_linux_amd64.deb && \
    sudo apt-get install -f

# Aptitude clear cache
RUN sudo apt-get clean

# Test
RUN aws --version
RUN sam --version