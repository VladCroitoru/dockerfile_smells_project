FROM circleci/python:3.7.2-stretch-node-browsers

ARG H=/home/circleci

# https://releases.hashicorp.com/terraform/0.9.11/terraform_0.9.11_linux_amd64.zip
RUN echo "alias ll='ls -alh'" >> ${H}/.bashrc && echo "set -o vi" >> ${H}/.bashrc

RUN sudo npm install -g yarn@latest yuglify@latest && sudo chmod +x /usr/local/bin/yarn

RUN sudo apt-get install rsync jq

RUN sudo apt-get update --fix-missing && sudo apt-get install -y \
  gdal-bin \
  --no-install-recommends

RUN sudo apt install -y vim

RUN whoami; \
cd /home/circleci; \
sudo pip install -U awscli boto3 requests python-digitalocean; \
pip --version; \
aws --version;

ADD build_container.bashrc /home/circleci/.bashrc

RUN curl -sL https://sentry.io/get-cli/ | bash; \
sudo /usr/local/bin/sentry-cli update

RUN sudo npm install -g sass


