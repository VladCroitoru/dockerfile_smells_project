FROM python:2.7-slim

COPY pre-requirements.txt requirements.txt /tmp/

RUN apt-get update && apt-get install -y libopenblas-dev libjpeg-dev --no-install-recommends

RUN set -x \
	&& buildDeps=' \
		curl \
		gcc \
		libbz2-dev \
		libncurses-dev \
		libreadline-dev \
		libsqlite3-dev \
		libssl-dev \
		make \
		zlib1g-dev \
		zip \
		unzip \
		gfortran \
		g++ \
		pkg-config \
		libfreetype6-dev \
	' \
	&& apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
	&& mkdir -p /usr/src/python \
	&& curl -SL "https://github.com/google/google-visualization-python/archive/master.zip" -o gviz_api.zip \
	&& unzip -o -j -qq gviz_api.zip -d /usr/src/python/gviz_api/ \
	&& rm gviz_api.zip \
	&& cd /usr/src/python/gviz_api \
	&& python ./setup.py install \
	&& cd .. \
	&& pip install --no-cache-dir --upgrade -r /tmp/pre-requirements.txt \
	&& pip install --no-cache-dir --upgrade -r /tmp/requirements.txt \
	&& find /usr/local \
		\( -type d -a -name test -o -name tests \) \
		-o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
		-exec rm -rf '{}' + \
	&& apt-get purge -y --auto-remove $buildDeps \
	&& rm -rf /usr/src/python

RUN python -m nltk.downloader -d /usr/local/share/nltk_data stopwords wordnet punkt

ENTRYPOINT ["python"]
