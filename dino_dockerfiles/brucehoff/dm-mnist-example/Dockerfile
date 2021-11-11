# https://hub.docker.com/r/dreamchall/tensorflow/
FROM dreamchall/tensorflow:devel-gpu
# not sure where 'convolutional.py' goes, so let's put it in both places
COPY convolutional.py /tensorflow/tensorflow/models/image/mnist/convolutional.py
COPY convolutional.py /usr/local/lib/python2.7/dist-packages/tensorflow/models/image/mnist/convolutional.py
COPY train.sh /train.sh
COPY test.sh /test.sh
