FROM tleyden5iwx/caffe-cpu-master

MAINTAINER Thanabhat Koomsubha "thanabhat@gmail.com"

RUN pip install git+https://github.com/Thanabhat/neuraltalk.git \
  && wget -O /usr/local/lib/python2.7/dist-packages/neuraltalk/python_features/VGG_ILSVRC_16_layers.caffemodel "http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel" \
  && wget -O /home/coco_cnn_lstm_v2.zip "http://cs.stanford.edu/people/karpathy/neuraltalk/coco_cnn_lstm_v2.zip" \
  && unzip /home/coco_cnn_lstm_v2.zip -d /usr/local/lib/python2.7/dist-packages/neuraltalk/model \
  && rm /home/coco_cnn_lstm_v2.zip

WORKDIR /home
