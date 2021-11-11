FROM nathanielrb/chicken
MAINTAINER "nathaniel.rudavsky@gmail.com"

ENV DEBUG false
ENV MU_SPARQL_ENDPOINT "http://database:8890/sparql"
ENV MU_DEFAULT_GRAPH "http://mu.semte.ch/application"
ENV DEFAULT_LANG "en"

ADD . /usr/src/app

RUN mkdir /logs && \
    echo "Installing eggs..." && \
    cat /usr/src/app/requirements.txt | xargs chicken-install

RUN cd `csi -p '(chicken-home)'` && \
    curl https://3e8.org/pub/chicken-doc/chicken-doc-repo.tgz | tar zx && \
    cd /

ONBUILD RUN cd /usr/src/app && \
         git submodule update --recursive --remote && \
         cd /usr/src/app/s-sparql && \
         chicken-install && \
         cd /usr/src/app/mu-chicken-support && \
         chicken-install

ONBUILD ADD . /app

ONBUILD RUN if [ -f /app/requirements.txt ]; then \
              echo "Installing eggs..." && \
              cat /app/requirements.txt | xargs chicken-install;\
            fi

ONBUILD RUN  echo "Compiling app.scm" && \
             cd /usr/src/app && \
             csc -include-path /app app.scm

EXPOSE 80
EXPOSE 4028

CMD cd /usr/src/app && \
    ./entrypoint.sh