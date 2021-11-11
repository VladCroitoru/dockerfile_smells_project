# Format: FROM    repository[:version]
FROM       ubuntu:16.04

# Usage:
# docker run -it -v <your directory>:/documents/


ENV DEBIAN_FRONTEND noninteractive

# Update apt-get sources AND install stuff
RUN apt-get update && apt-get install -y -q texlive texlive-latex-extra texlive-lang-cjk python-pip make latexmk git
RUN pip install --upgrade pip
RUN pip install Sphinx
RUN pip install recommonmark
RUN pip install sphinxcontrib-textstyle
## tk0miya's *diag series
RUN pip install sphinxcontrib-blockdiag sphinxcontrib-nwdiag sphinxcontrib-seqdiag sphinxcontrib-actdiag

RUN mkdir documents

WORKDIR /documents
VOLUME /documents

CMD ["/bin/bash"]
