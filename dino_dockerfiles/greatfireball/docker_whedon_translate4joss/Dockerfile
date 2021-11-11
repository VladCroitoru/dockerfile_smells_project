ARG osversion=xenial
FROM ubuntu:${osversion}

ARG VERSION=master
ARG VCS_REF
ARG BUILD_DATE

RUN echo "VCS_REF: "${VCS_REF}", BUILD_DATE: "${BUILD_DATE}", VERSION: "${VERSION}

LABEL maintainer="frank.foerster@ime.fraunhofer.de" \
      description="Dockerfile providing the whedon installation for a preview of joss submissions" \
      version=${VERSION} \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.vcs-url="https://github.com/greatfireball/docker_whedon_translate4joss.git"

ENV WHEDON_DIR=/opt/whedon

RUN apt update && \
    apt install --yes --no-install-recommends \
       biber \
       git \
       lmodern \
       pandoc \
       pandoc-citeproc \
       texlive-xetex \
       texlive \
       texlive-latex-extra \
       texlive-bibtex-extra \
       texlive-fonts-recommended \
       wget && \
    wget -O /tmp/pandoc.deb https://github.com/jgm/pandoc/releases/download/2.1.1/pandoc-2.1.1-1-amd64.deb && \
    dpkg -i /tmp/pandoc.deb && \
    git clone https://github.com/openjournals/whedon.git "${WHEDON_DIR}"

VOLUME /data
WORKDIR /data

ENTRYPOINT pandoc -o paper.pdf -V geometry:margin=1in --filter pandoc-citeproc paper.md --template "${WHEDON_DIR}"/resources/latex.template --variable formatted_doi=pending -V joss_logo_path="${WHEDON_DIR}"/resources/joss-logo.png --pdf-engine=xelatex

CMD "--variable=repository:https://link-to-repo --variable=archive_doi:https://archive-doi"
