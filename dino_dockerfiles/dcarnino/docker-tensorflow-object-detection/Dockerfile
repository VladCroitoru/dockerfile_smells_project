FROM tensorflow/tensorflow:1.6.0-devel-gpu-py3

RUN apt-get update
RUN apt-get install -y python3-tk protobuf-compiler python3-lxml git\
    && pip3 install Cython

RUN mkdir -p /tensorflow/models
RUN git clone https://github.com/dcarnino/models.git /tensorflow/models

RUN git clone https://github.com/cocodataset/cocoapi.git \
    && cd cocoapi/PythonAPI \
    && python3 setup.py build_ext --inplace \
	&& rm -rf build \
    && cp -r pycocotools /tensorflow/models/research/ \
    && cd ../../

WORKDIR /tensorflow/models/research
RUN sed -i '87d' object_detection/protos/ssd.proto \
    && sed -i -e "168s/range(num_boundaries)/list(range(num_boundaries))/" object_detection/utils/learning_schedules.py
RUN protoc object_detection/protos/*.proto --python_out=.

RUN pip3 install --upgrade pip \
    && pip3 install --upgrade dask \
    && pip3 install pandas \
    && pip3 install Pillow
    
RUN pip3 install tf-nightly-gpu==1.9.0.dev20180503

RUN python3 setup.py sdist \
    && (cd slim && python3 setup.py sdist)

ENV PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
