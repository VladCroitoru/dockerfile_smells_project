# The purpose of this Dockerfile is for me to try out pyenv and pyvenv without screwing up my machine.
# Traditionally, I've just used either python (for Python 2) or python3 (for 3), with virtualenvwrapper
# for managing virutal environments.  The two drawbacks to this approach are remembering the different
# commands for invoking python, and that virtualenvwrapper "clouds up" the environmnet namespace with
# a ton of verbs like workon, mkvirtualenv, setproject etc.  I like the way pyenv and pyvenv solve both
# these problems and will most likely use this approach for all my Python dev in the future.
FROM bradleybossard/docker-common-devbox
MAINTAINER Bradley Bossard <bradleybossard@gmail.com>

# Build the image
# docker build --rm -t docker-python-devbox .

# Fire up an instance with a bash shell
# docker run --rm -i -t docker-python-devbox

# Update ubuntu
RUN apt-get update

# Need git to install pyenv and pyvenv-virtualenv
RUN apt-get install -y git
# pyenv dependencies to compile python versions
RUN apt-get install -y make \
  build-essential \
  libssl-dev \
  zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  # Python tools
  python-pip \
  python-virtualenv

# Change to python_user home dir and change to user python_user
WORKDIR /root

# Download pyenv and add it to the python_user .bashrc
RUN git clone https://github.com/yyuu/pyenv.git .pyenv
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> .bashrc
RUN echo 'export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"' >> .bashrc
RUN echo 'eval "$(pyenv init -)"' >> .bashrc

# Download pyvenv-virtualenv and add it to the python_user .bashrc
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git .pyenv/plugins/pyenv-virtualenv
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> .bash_profile

# Add the same PATH variables from above to current environment,
# needed for the next install steps
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Install some pythons
RUN pyenv install 2.7.10
RUN pyenv install 3.4.3
RUN pyenv rehash
RUN pyenv global 3.4.3 

RUN pip install --upgrade pip

