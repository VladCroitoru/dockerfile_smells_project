FROM philopon/py3-rdkit
MAINTAINER Hiroyuki YAMASAKI <yamasakih@pharm.kitasato-u.ac.jp>

USER root
RUN apk --no-cache --update-cache add gcc g++ python3-dev 
RUN pip3 uninstall -y numpy
RUN pip3 install --no-cache-dir numpy chainer-chemistry
