FROM maven:3-jdk-8

ENV WORKSPACE=/opt/pattern_pipeline
ENV DATA=/data
ENV CORPUS=${DATA}/corpus
ENV DATAOUT=${DATA}/out

VOLUME ${DATA}

RUN echo Building Pattern Analysis Pipeline && \
mkdir -p ${WORKSPACE} && \
cd ${WORKSPACE} && \
git clone https://github.com/matentzn/ontologyinferenceanalysis && \
git clone https://github.com/matentzn/patternextract && \
git clone https://github.com/matentzn/corpusdebugger && \
git clone https://github.com/matentzn/ebi.utilities && \
cd ${WORKSPACE}/ebi.utilities && \
mvn clean install && \
cd ${WORKSPACE}/patternextract && \
mvn clean compiler:compile package && \
cp target/pattern.extract-1.0-jar-with-dependencies.jar ${WORKSPACE}/patternextract.jar && \
cd ${WORKSPACE}/corpusdebugger && \
mvn clean compiler:compile package && \
cp target/corpus.debugger-1.0-jar-with-dependencies.jar ${WORKSPACE}/corpusdebugger.jar && \
cd ${WORKSPACE}/ontologyinferenceanalysis && \
mvn clean compiler:compile package && \
cp target/ontology.inferenceanalysis-1.0-jar-with-dependencies.jar ${WORKSPACE}/inferenceanalysis.jar && \
rm -r ${WORKSPACE}/patternextract && \
rm -r ${WORKSPACE}/corpusdebugger && \
rm -r ${WORKSPACE}/ontologyinferenceanalysis

COPY run.sh ${WORKSPACE}/run.sh
COPY pattern_analysis.Rmd ${WORKSPACE}/pattern_analysis.Rmd

RUN chmod +x ${WORKSPACE}/run.sh

ENTRYPOINT ["/opt/pattern_pipeline/run.sh"]
