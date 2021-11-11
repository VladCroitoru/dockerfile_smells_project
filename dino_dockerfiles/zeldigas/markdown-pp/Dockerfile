FROM python:3.6

RUN curl https://github.com/jreese/markdown-pp/archive/v1.3.tar.gz -L > archive.tgz \
	&& tar xf archive.tgz \
	&& pip install ./markdown-pp-1.3 \
	&& rm -rf archive.zip markdown-pp-1.3

RUN mkdir -p /wd

WORKDIR /wd

	
