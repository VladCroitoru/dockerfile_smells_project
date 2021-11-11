FROM ubuntu:xenial
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
        apt-get install -y software-properties-common && \
        add-apt-repository ppa:deadsnakes/ppa && \
        apt-get update -y  && \
        apt-get install -y build-essential python3.6 python3.6-dev python3-pip && \
        apt-get install -y git  && \
        # update pip
        python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get -y install python-pip liblapack3 libblas-dev liblapack-dev gfortran
RUN apt-get update
#RUN apt-get install vim
# RUN apt-get -y install nvidia-container-runtime
RUN apt-get -y install vim

RUN pip install numpy
RUN pip install nibabel
RUN pip install --upgrade lxml
RUN pip install -U scikit-learn
RUN pip install tables
RUN pip install scikit-image
RUN pip install requests-toolbelt
RUN pip install requests==2.10.0
RUN apt-get -y install python-lxml


RUN mkdir /module
RUN mkdir /module/source
WORKDIR /module
COPY ./public /module
COPY ./bqapi /module/bqapi


COPY PythonScriptWrapper /module/
COPY PythonScriptWrapper.py /module/
# COPY source  /module/
# COPY pydist /module/pydist/
# RUN python setup.py install && cd ..
COPY GobjectAdd.py /module/


ENV PATH /module:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

CMD [ 'PythonScriptWrapper' ]
