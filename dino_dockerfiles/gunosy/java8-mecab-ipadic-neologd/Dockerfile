FROM java:8
ENV NEOLOGD_PATH=/usr/local/lib/neologd
ENV NEOLOGD_WORK=/tmp/neologd

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential file
RUN apt-get install -y mecab=0.996-1.1 libmecab-dev=0.996-1.1 mecab-ipadic-utf8
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir -p ${NEOLOGD_PATH} ${NEOLOGD_WORK}
WORKDIR ${NEOLOGD_WORK}
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
    mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y -p ${NEOLOGD_PATH}
RUN rm -rf ${NEOLOGD_WORK}

