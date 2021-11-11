FROM python:3.4.2

MAINTAINER Kazuki Fukui

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	git \
	sqlite3 libsqlite3-dev \
	mecab libmecab-dev mecab-ipadic-utf8 && \
	apt-get -y autoremove && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

RUN pip install mecab-python3 pandas requests
RUN git clone https://github.com/oshikiri/shirimas.git --recursive

WORKDIR shirimas/src
RUN touch mysetup.py

VOLUME /shirimas/src/db
CMD python3 autoexec.py

