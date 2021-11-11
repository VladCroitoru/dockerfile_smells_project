FROM tleyden5iwx/caffe-cpu-master

RUN apt-get update

RUN apt-get -y --force-yes install python python-dev python-pip build-essential git

RUN pip install pandas matlab numpy jupyter

RUN pip install scikit-image

RUN apt-get -y --force-yes install imagemagick && pip install pillow

RUN pip install flask flask-restful

RUN mkdir /models && cd /models && wget http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel

RUN sh /opt/caffe/data/ilsvrc12/get_ilsvrc_aux.sh

WORKDIR /home
RUN git clone https://github.com/mbartoli/GoogLeNet-API
WORKDIR /home/GoogLeNet-API/api

EXPOSE 3000
CMD ["python", "api.py"]
