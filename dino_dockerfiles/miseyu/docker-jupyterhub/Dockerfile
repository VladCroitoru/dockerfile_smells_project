FROM ubuntu:14.04

# require library install
RUN apt-get -q -y update \
  && apt-get -q -y install git wget curl tar \
  && apt-get -q -y install git gcc g++ make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev python-dev \
  && apt-get -q -y install python3-matplotlib libfreetype6-dev libxft-dev \
  && apt-get -q -y clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# nodejs and npm
RUN wget -O - http://nodejs.org/dist/v0.10.23/node-v0.10.23.tar.gz | tar xvzf - && \
    cd node-v0.10.23 && ./configure --prefix=/usr && make && make install

# pyenv and python3 install
RUN cd /usr/local/ \
  && git clone git://github.com/yyuu/pyenv.git ./pyenv \
  && mkdir -p ./pyenv/versions ./pyenv/shims \
  && echo 'export PYENV_ROOT=/usr/local/pyenv' | tee -a /etc/profile.d/pyenv.sh \
  && echo 'export PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH' | tee -a /etc/profile.d/pyenv.sh \
  && export PYENV_ROOT=/usr/local/pyenv \
  && export PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH \
  && pyenv install -v 3.4.3 \
  && pyenv global 3.4.3 \
  && pyenv rehash \
  && pip install --upgrade pip && pip install pandas \
  && npm install -g configurable-http-proxy \
  && pip install zmq jsonschema \
  && pip install matplotlib ipython-sql \
  && pip install ipython[notebook] jupyterhub

RUN useradd admin -m && echo "admin:admin" | chpasswd

ADD jupyterhub_config.py /usr/local/jupyterhub_config.py

EXPOSE 8000
CMD  cd /usr/local && export PYENV_ROOT=/usr/local/pyenv && export PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH && jupyterhub -f /usr/local/jupyterhub_config.py
