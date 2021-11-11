FROM python:3

WORKDIR /opt/pattern_pipeline

ENV WORKSPACE=/opt/dipper
ENV DATA=/data
ENV CORPUS=${DATA}/corpus
ENV DATAOUT=${DATA}/out

ENV JAVA_OPTS='-Xmx20g -Xms12g'

VOLUME ${DATA}

RUN echo Building Dipper && \
mkdir -p ${WORKSPACE} && \
cd ${WORKSPACE} && \
git clone https://github.com/monarch-initiative/dipper && \
cd ${WORKSPACE}/dipper && \
pip3 install -r requirements.txt && \
pip3 install -r requirements/all-sources.txt

COPY run.sh ${WORKSPACE}/run.sh
RUN chmod +x ${WORKSPACE}/run.sh

ENTRYPOINT ["/opt/dipper/run.sh"]
