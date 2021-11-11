FROM ubuntu:16.04
MAINTAINER Soichi Hayashi <hayashis@iu.edu>

RUN apt-get update && apt-get install -y python-pip
RUN apt-get install -y xvfb x11-xkb-utils
RUN apt-get install -y xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
RUN apt-get install -y python-matplotlib python-vtk

RUN pip install numpy cython scipy h5py nibabel nipype
RUN pip install cvxpy scikit-learn
#dipy >0.14 doesn't have dipy.viz.window
RUN pip install dipy==0.14.0 joblib pandas nibabel

RUN pip install xvfbwrapper

#make it work under singularity
RUN ldconfig && mkdir -p /N/u /N/home /N/dc2 /N/soft

#prevent ~/.local from getting loaded (doesn't look like it's working..?)
ENV PYTHONNOUSERSITE=true

#https://wiki.ubuntu.com/DashAsBinSh
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
