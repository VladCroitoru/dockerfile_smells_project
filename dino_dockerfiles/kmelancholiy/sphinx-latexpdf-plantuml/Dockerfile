FROM python:3

ENV PLANTUML_DIR /usr/local/plantuml
ENV PLANTUML_JAR plantuml.jar
ENV PLANTUML ${PLANTUML_DIR}/${PLANTUML_JAR}

RUN set -x \
 && apt-get update \
 && apt-get install -y \
    git texlive-full texlive-lang-cjk \
    wget default-jre graphviz \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && true
RUN set -x \
 && mkdir ${PLANTUML_DIR} \
 && wget "https://sourceforge.net/projects/plantuml/files/plantuml.jar" --no-check-certificate \
 && mv plantuml.jar ${PLANTUML} \
 && true
RUN set -x \
 && pip install \
    sphinx \
    sphinxcontrib-blockdiag \
    sphinxcontrib-actdiag \
    sphinxcontrib-nwdiag \
    sphinxcontrib-seqdiag \
    sphinxcontrib-plantuml \
 && echo "Done."

CMD ["/bin/bash"]
