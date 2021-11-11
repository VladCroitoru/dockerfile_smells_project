FROM ubuntu:14.04

ENV HOSTNAME dataworkshop

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install build-essential && \
    apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 git vim
	
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

#   Add Tini - tini 'init' for containers
RUN apt-get install -y curl grep sed dpkg && \
    ## static version assignment
    ## ENV TINI_VERSION v0.10.0 && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean
	
# Install anaconda
ENV PATH /opt/conda/bin:$PATH
RUN cd /opt/conda/bin && \
    conda install -c conda-forge jupyterlab -y --quiet && \
    conda install -c conda-forge jupyter_contrib_nbextensions -y && \
    conda install -c https://conda.anaconda.org/menpo opencv -y && \
    jupyter serverextension enable --py jupyterlab && \
    mkdir /opt/notebooks

RUN pip install --upgrade pip

# build xgboost from source
RUN cd /usr/local/src && \
    git clone --recursive https://github.com/dmlc/xgboost.git && cd xgboost && ./build.sh && cd python-package && python setup.py install

# install python libraries required for dataworkshop
COPY extra_packages.txt /tmp/
RUN pip install -r /tmp/extra_packages.txt

# plotting on maps
#RUN pip install gmplot && \
#    pip install folium
## problem with geoplotlib import - pip install correct, but lack of geoplotlib.gl module
## pip install geoplotlib && \
## 276 MB danych
# apt-get -y install libgdal-dev && \
# pip install vincent && \
## 134MB
# conda install -c anaconda basemap -y --quiet && \
## 90MB
# conda install -c conda-forge geopandas -y --quiet

COPY .keras/keras.json /root/.keras/keras.json

## get script with prerequisites
RUN pip install clint && \
    git clone https://github.com/dataworkshop/prerequisite /opt/prerequisite

# Add start script to launch jupyter notebook and jupyter lab in the background
COPY start_script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start_script.sh

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["/usr/local/bin/start_script.sh"]
