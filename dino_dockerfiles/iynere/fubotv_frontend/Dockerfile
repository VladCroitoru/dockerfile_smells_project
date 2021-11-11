FROM circleci/node:6.11

USER root

# install python-dev
RUN apt-get install -y python-dev

# install pip & awscli
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py && \
    pip install awscli

# install static-server for deployments
RUN yarn global add static-server

USER circleci