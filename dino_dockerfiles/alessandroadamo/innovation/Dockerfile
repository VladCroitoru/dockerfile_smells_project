FROM continuumio/anaconda3

MAINTAINER Alessandro Adamo <alessandro.adamo@gmail.com>

USER root

RUN apt-get -qq update && apt-get -y dist-upgrade

RUN apt-get install -y \
	curl \
	gcc \
	g++ \
	gfortran \
	build-essential \
	locales \
	unixodbc \
	libaio1 \
	bc \
	flex \
	fonts-dejavu \
	supervisor \
	libgl1-mesa-dev \
	libgl1-mesa-glx

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# supervisor for multi entry points
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN locale-gen

# Hacky access control for the image
RUN adduser --disabled-password --gecos '' innovation
RUN echo "innovation ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN apt-get clean -y && apt-get clean -y && apt-get -y autoremove

# Install Oracle client
RUN conda install -c anaconda -y oracle-instantclient=11.2.0.4

# install jupyter 
RUN conda install -y jupyter ipykernel

WORKDIR /tmp
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz
RUN mkdir -p /opt/jdk
RUN tar xvfz /tmp/jdk-8u131-linux-x64.tar.gz -C /opt/jdk
ENV JAVA_HOME /opt/jdk/jdk1.8.0_131
ENV PATH ${JAVA_HOME}/bin:$PATH
RUN update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_131/bin/java 100
RUN update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_131/bin/javac 100
RUN rm /tmp/jdk-8u131-linux-x64.tar.gz

# # install Spark
ADD https://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz /opt/ 
RUN ln -s /opt/spark-2.1.0-bin-hadoop2.7 /opt/spark
ENV SPARK_HOME /opt/spark
ENV PATH ${SPARK_HOME}/sbin:${SPARK_HOME}/bin:${PATH}
ENV PYTHONPATH ${SPARK_HOME}/python/:${PYTHONPATH}
ENV PYTHONPATH ${SPARK_HOME}/python/lib/py4j-0.10.4-src.zip:${PYTHONPATH}
 
ENV PYSPARK_DRIVER_PYTHON="jupyter"
ENV PYSPARK_DRIVER_PYTHON_OPTS="notebook"

# install packages anaconda
RUN /opt/conda/bin/conda install -c conda-forge -y \
	pip \
	numpy \
	scipy \
	pandas \
	pandas-datareader \
	geopandas\
 	polyline \
	geopy \
	rtree \
	descartes \
	pytables \
	matplotlib \
	bokeh \
	plotly \
	shapely \
	basemap \
	curl \
	iso8601 \
	urllib3 \
	memory_profiler \
	line_profiler \
	psutil \
#	nltk \
	gensim \
	pcre \
	scikit-learn \
	tensorflow \
	seaborn \
	sympy \
	pysal \
	keras \
	hdf5 \
	google-api-python-client \
	networkx \
	nxviz \
	geographiclib
RUN /opt/conda/bin/conda update dask
RUN /opt/conda/bin/conda clean -yat

# install Tensorflow
# RUN /opt/conda/bin/pip install --upgrade dask
# RUN /opt/conda/bin/pip install --upgrade tensorflow
# RUN /opt/conda/bin/pip install --upgrade tensorflow-tensorboard 
# RUN /opt/conda/bin/pip install --upgrade tflearn

RUN conda install -c mgckind cx_oracle=5.3
RUN conda install -c glemaitre imbalanced-learn

RUN /opt/conda/bin/pip install \
	gmplot \
	geographiclib

RUN /opt/conda/bin/pip install hug
RUN /opt/conda/bin/pip install Flask

# RUN /opt/conda/bin/pip install -i https://pypi.anaconda.org/pypi/simple googlemaps 

# # R packages including IRKernel which gets installed globally.
RUN conda install -c conda-forge -y \
 	rpy2 \
	r-base \
	r-essentials \
	r-spatial \
	r-irkernel \
	r-devtools \
	r-tidyverse \
	r-shiny \
	r-rmarkdown \
	&& conda clean -tipsy

RUN conda install -c mgckind cx_oracle=5.3

RUN cp -p /lib/x86_64-linux-gnu/libreadline.so.6 /opt/conda/lib/libreadline.so.6

# # install R packages
ADD install.R /tmp/install.R
RUN /opt/conda/bin/Rscript /tmp/install.R

RUN /bin/bash -c ""

RUN chown -Rf innovation /var/log/supervisor/
USER innovation
RUN mkdir -p /home/innovation/notebooks
RUN mkdir -p /home/innovation/tf_logs
WORKDIR /home/innovation

# install NLTK download
# RUN /opt/conda/bin/python3 -m nltk.downloader all

# Jupyter
EXPOSE 8888
# TensorBoard
EXPOSE 6006

# Hug port range
EXPOSE 8000-8050 

ENTRYPOINT ["/usr/bin/supervisord", "--conf=/etc/supervisor/conf.d/supervisord.conf"]

