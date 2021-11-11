FROM ubuntu:xenial

RUN apt-get -y update
RUN apt-get -y install python2.7 python-pip python-dev ipython ipython-notebook
RUN pip install --upgrade pip
RUN pip install jupyter

RUN apt-get -y install nodejs-legacy npm
RUN npm install -g jp-babel jp-coffeescript
RUN jp-babel-install
RUN jp-coffee-install

ENV NODE_PATH=/node_modules

CMD jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root
