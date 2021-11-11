FROM ubuntu

# Update the package index
RUN apt-get update -y

# Install all requirements of pyenv
# See: https://github.com/pyenv/pyenv/wiki/Common-build-problems#requirements
RUN apt-get install -y sudo make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev

# Install git and bash (used by pyenv-installer)
RUN apt-get install -y git
RUN apt-get install -y bash

# Install pyenv as recommended:
# https://github.com/pyenv/pyenv-installer
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
ENV PATH="/root/.pyenv/bin:$PATH"
RUN eval "$(pyenv init -)" && eval "$(pyenv virtualenv-init -)"

# Install Python pip
RUN apt-get install -y python-pip && pip install --upgrade pip
