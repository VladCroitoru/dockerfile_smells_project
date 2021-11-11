# This is a comment
FROM rugcompling/alpino:latest
MAINTAINER Wouter van Atteveldt (wouter@vanatteveldt.com)
EXPOSE 5002

# Get and unpack NERC models
RUN mkdir models && curl http://i.amcat.nl/nerc-models-1.5.4-nl.tgz | tar xz -C models

RUN apt-get -qq update && apt-get install -y git python-flask python-pip python-lxml openjdk-7-jdk maven 
RUN pip install KafNafParserPy

# Install tokenizer
RUN git clone https://github.com/ixa-ehu/ixa-pipe-tok && (cd ixa-pipe-tok && mvn -Dmaven.compiler.target=1.7 -Dmaven.compiler.source=1.7 clean package)

# Install morphosyntactic parser
RUN git clone https://github.com/cltl/morphosyntactic_parser_nl

# Install NERC 
RUN git clone https://github.com/ixa-ehu/ixa-pipe-nerc && (cd ixa-pipe-nerc && mvn -Dmaven.compiler.target=1.7 -Dmaven.compiler.source=1.7 clean package)

COPY run_pipeline.sh server.py ./
CMD python server.py --host 0.0.0.0 --port 5002 --debug
