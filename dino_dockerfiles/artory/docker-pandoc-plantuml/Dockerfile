FROM haskell:8.0.2

RUN cabal update && cabal install pandoc
RUN apt-get update && apt-get -y install default-jre curl graphviz

COPY plantuml /usr/local/bin/plantuml
RUN curl -sSL http://sourceforge.net/projects/plantuml/files/plantuml.1.2017.13.jar/download > /usr/local/bin/plantuml.jar && chmod +x /usr/local/bin/plantuml
COPY pandoc-plantuml /usr/local/bin/
RUN chmod +x /usr/local/bin/pandoc-plantuml
