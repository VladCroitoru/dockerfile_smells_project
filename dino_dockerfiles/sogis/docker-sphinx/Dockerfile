#FROM ubuntu:latest # LTS
FROM ubuntu:17.04

# Usage:
# docker run -it -v <your directory>:/documents/

ENV DEBIAN_FRONTEND noninteractive

# Update apt-get sources AND install stuff
RUN apt-get update && apt-get install -y -q python-sphinx python-sphinx-rtd-theme python-sphinx-bootstrap-theme texlive texlive-latex-extra texlive-lang-german pandoc build-essential

RUN mkdir documents

WORKDIR /documents
VOLUME /documents

CMD ["/bin/bash"]