FROM jupyter/scipy-notebook

MAINTAINER Jay <jaikumarm@yahoo.com>

USER root
RUN apt-get update && apt-get install -yq curl && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

RUN curl -L http://downloads.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz > ta-lib-0.4.0-src.tar.gz &&\ 
	tar xvzf ta-lib-0.4.0-src.tar.gz && cd ta-lib && \
	./configure --prefix=/usr && \
	make && make install &&\
	cd .. && rm ta-lib-0.4.0-src.tar.gz && rm -r ta-lib

USER jovyan

RUN conda install --quiet --yes -c jaikumarm \
	'theano=0.9.0.dev2' \
	'keras=1.0.8' \
	'hyperopt=0.0.3.dev3' \
	'ta-lib=0.4.9' \
	'deap=1.0.2' \
	'tpot=0.4.1.parallelize' \
	'hyperas=0.3.dev' \
	'flatdict=1.2.0' \
	&& conda clean -tipsy

RUN conda install --quiet --yes psycopg2 \
	&& conda clean -tipsy

#RUN pip install deap xgboost tpot
