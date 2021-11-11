# Build: docker build pandashells .
# Usage: docker run -it -v ${pwd}/data:/data pandashells
FROM python:3.5

MAINTAINER https://github.com/robdmc/pandashells 

ENV REFRESHED_AT 2015-08-03

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
  apt-transport-https \
  build-essential \
  libopenblas-dev \
  libatlas-dev \
  liblapack-dev \
  gfortran \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN env --unset=DEBIAN_FRONTEND

# cost of layering is better than cost of rebuilding
RUN pip3 install numpy
RUN pip3 install astroML
RUN pip3 install scipy
RUN pip3 install scikit-learn
RUN pip3 install supersmoother
RUN pip3 install gatspy
RUN pip3 install mpld3
RUN pip3 install pandas
RUN pip3 install pandashells
RUN pip3 install matplotlib
RUN pip3 install seaborn
RUN pip3 install statsmodels

VOLUME /data
WORKDIR /data

RUN groupadd -r po && useradd -r -g po po
USER po

CMD ["bash"]
