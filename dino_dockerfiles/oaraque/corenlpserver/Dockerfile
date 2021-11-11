FROM java:8-jre-alpine
MAINTAINER Oscar Araque

RUN mkdir /corenlp
WORKDIR /corenlp

RUN apk add --update ca-certificates openssl && update-ca-certificates

RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip
RUN unzip *.zip && rm *.zip
WORKDIR ./stanford-corenlp-full-2018-10-05/

RUN wget http://nlp.stanford.edu/software/stanford-french-corenlp-2018-10-05-models.jar
RUN wget http://nlp.stanford.edu/software/stanford-spanish-corenlp-2018-10-05-models.jar
RUN wget https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP-french.properties
RUN wget https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP-spanish.properties
RUN wget https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP.properties

ENV JAVA_OPTS -Xmx3g
ENV PORT 9000
ENV SERVER_PROPERTIES StanfordCoreNLP.properties

CMD java $JAVA_OPTS -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties $SERVER_PROPERTIES -port $PORT
