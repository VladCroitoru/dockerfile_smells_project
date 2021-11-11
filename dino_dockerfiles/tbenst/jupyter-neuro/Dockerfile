FROM continuumio/anaconda3:4.0.0p0
MAINTAINER Tyler Benster

EXPOSE 8888

RUN mkdir /notebooks

# TODO install octave and chronux
# RUN apt-get update && apt-get install -y \
#   octave \
#   unzip

# RUN wget http://chronux.org/chronuxFiles/filesReleases/chronux_2_12.zip

RUN conda install bokeh scikit-learn

ARG CACHE_DATE=2017-03-28
RUN git clone -b acuity https://github.com/tbenst/glia.git
WORKDIR glia
RUN pip install -r requirements.txt
RUN python setup.py install

ADD custom.js /root/.jupyter/custom/
VOLUME /notebooks
WORKDIR /notebooks

CMD jupyter notebook --no-browser --ip=0.0.0.0