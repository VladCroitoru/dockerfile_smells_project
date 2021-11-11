FROM python:3.6

ENV SPHINX_VERSION 1.6.2
ENV SPHINX_BOOTSTRAP_VERSION 0.5.3
ENV SPHINX_RTD_VERSION 0.2.5b1

RUN apt-get update && apt-get install -y librsvg2-bin && apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	pip install sphinx==$SPHINX_VERSION sphinx-bootstrap-theme==$SPHINX_BOOTSTRAP_VERSION sphinx-rtd-theme==$SPHINX_RTD_VERSION
