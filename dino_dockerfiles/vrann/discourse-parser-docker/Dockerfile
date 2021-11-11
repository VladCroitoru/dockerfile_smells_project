#FROM python:2.7.8
FROM java:7

MAINTAINER Eugene Tulika "vranen@gmail.com"

# Install Python.
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

RUN wget http://pyyaml.org/download/pyyaml/PyYAML-3.09.tar.gz \ 
	&& tar -zxf PyYAML-3.09.tar.gz \
	&& cd PyYAML-3.09 \
	&& python setup.py install

RUN wget https://pypi.python.org/packages/source/n/nltk/nltk-2.0b9.tar.gz \
	&& tar -zxf nltk-2.0b9.tar.gz \
	&& cd nltk-2.0b9 \
	&& python setup.py install

RUN wget http://www.cs.toronto.edu/~weifeng/software/discourse_parse-2.01.tar.gz \
	&& tar -zxf discourse_parse-2.01.tar.gz \
        && cd gCRF_dist/tools/crfsuite

RUN wget https://github.com/downloads/chokkan/liblbfgs/liblbfgs-1.10.tar.gz \
	&& tar -zxf liblbfgs-1.10.tar.gz \
        && cd liblbfgs-1.10 \
        && ./configure --prefix=$HOME/local \
        && make \
        && make install

RUN cd gCRF_dist/tools/crfsuite/crfsuite-0.12 \
	&& chmod +x configure \
        && ./configure --prefix=$HOME/local --with-liblbfgs=$HOME/local \
	&& make \
	&& make install

RUN cd gCRF_dist/tools/crfsuite && \
	cp $HOME/local/bin/crfsuite crfsuite-stdin \
	&& chmod +x crfsuite-stdin

RUN cd gCRF_dist/tools/crfsuite \
	&& ./crfsuite-stdin tag -pi -m ../../model/tree_build_set_CRF/label/intra.crfsuite test.txt

CMD ["/bin/sh"]        

