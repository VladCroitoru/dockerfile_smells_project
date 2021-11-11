
FROM ubuntu:16.04

ENV SPHINX_VERSION 1.7.6
ENV SPHINX_BOOTSTRAP_VERSION 0.5.3
ENV SPHINX_RTD_VERSION 0.4.0

RUN rm -rf /var/lib/apt/lists/* && apt-get update && apt-get clean && \
	 apt-get install -y python2.7 python-pip librsvg2-bin && \
	pip install sphinx==$SPHINX_VERSION sphinx-bootstrap-theme==$SPHINX_BOOTSTRAP_VERSION sphinx-rtd-theme==$SPHINX_RTD_VERSION
RUN pip install sphinxcontrib-versioning
RUN pip install sphinxcontrib-httpdomain
RUN pip install sphinxcontrib-httpexample
RUN pip install sphinxcontrib-fulltoc
RUN pip install rst2pdf
RUN apt-get install -y texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended 
