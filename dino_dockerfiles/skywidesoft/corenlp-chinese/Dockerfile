FROM openjdk:8-jre
MAINTAINER Clarence Ho <clarence@skywidesoft.com>

RUN apt-get update \
    && wget http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip \
    && unzip stanford-corenlp-full-2017-06-09.zip \
    && rm stanford-corenlp-full-2017-06-09.zip

WORKDIR stanford-corenlp-full-2017-06-09

RUN wget http://nlp.stanford.edu/software/stanford-chinese-corenlp-2017-06-09-models.jar \
    && wget http://nlp.stanford.edu/software/stanford-english-corenlp-2017-06-09-models.jar

ENV PORT 9000

EXPOSE $PORT

CMD java -Xmx8g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-chinese.properties -port 9000 -timeout 15000
