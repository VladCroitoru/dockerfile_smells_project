FROM phusion/baseimage:latest

# Setup build environments for Python and Node.js
RUN apt-get update && apt-get install -y git make build-essential \
        libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
        wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev

# Version managers for Python and Node.js
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
RUN curl -L https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash

# Install Python
RUN echo 'export PATH="~/.pyenv/bin:${PATH}"' >> ~/.bashrc && \
        echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
        echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
RUN ${HOME}/.pyenv/bin/pyenv install 3.6.2
ENV PYENV_VERSION=3.6.2
RUN curl -L https://bootstrap.pypa.io/get-pip.py | ${HOME}/.pyenv/shims/python3.6

# Install Node.js (liberally borrowed from creationix/nvm Dockerfile
RUN bash -c 'source ${HOME}/.nvm/nvm.sh && \
        nvm install node'

# Install various packages, this is last to prevent cache busting.
RUN ${HOME}/.pyenv/shims/pip3 install jupyter matplotlib pandas scikit-learn flask flask-sqlalchemy
RUN bash -c 'source ${HOME}/.nvm/nvm.sh && \
        npm install -g create-react-app react react-dom react-script \
                react-c3js'

# Volume mount for project workspace
VOLUME ["/root/workspace"]

# Node development server
EXPOSE 3000
# Jupyter notebook default port
EXPOSE 8888
