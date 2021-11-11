FROM phusion/baseimage:latest

RUN apt-get update && apt-get install -y git make build-essential \
        libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
        wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
RUN echo 'export PATH="~/.pyenv/bin:${PATH}"' >> ~/.bashrc && \
        echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
        echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
RUN ${HOME}/.pyenv/bin/pyenv install 3.6.2
ENV PYENV_VERSION=3.6.2
RUN curl -L https://bootstrap.pypa.io/get-pip.py | ${HOME}/.pyenv/shims/python3.6
RUN ${HOME}/.pyenv/shims/pip3 install jupyter matplotlib pandas scikit-learn flask flask-sqlalchemy
