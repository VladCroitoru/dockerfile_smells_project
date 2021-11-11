FROM r-base

ENV DATA=/data

ENV WORKSPACE=/opt/knitr

VOLUME ${DATA}

RUN echo Building knitR Pipeline ${WORKSPACE} && \
mkdir -p ${WORKSPACE} && \
R -e "install.packages('knitr', repos = 'http://cran.us.r-project.org')"

COPY run.sh ${WORKSPACE}/run.sh
RUN chmod +x ${WORKSPACE}/run.sh

ENTRYPOINT ["/opt/knitr/run.sh"]
