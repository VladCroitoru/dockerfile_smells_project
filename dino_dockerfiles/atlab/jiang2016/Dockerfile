FROM datajoint/datajoint:0.3

MAINTAINER Fabian Sinz <sinz@bcm.edu>

RUN pip install jupyter

WORKDIR /jiang2016

ADD . /jiang2016

RUN pip install -e .

ENTRYPOINT /usr/local/bin/jupyter notebook --port=8888 --no-browser --ip=0.0.0.0
  
