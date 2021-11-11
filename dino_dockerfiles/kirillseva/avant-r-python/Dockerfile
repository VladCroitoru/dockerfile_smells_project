FROM kirillseva/avant-r-new
MAINTAINER kirillseva "https://github.com/kirillseva"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python python-setuptools python-pip python-virtualenv \
                       build-essential git python-dev gfortran libblas-dev \
                       libatlas-dev liblapack-dev

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
RUN mkdir -p /dev

# xgboost
RUN cd /dev && git clone https://github.com/dmlc/xgboost.git \
    && cd xgboost && git checkout 0.47 && ./build.sh && cd python-package && python setup.py install

CMD ["python"]
