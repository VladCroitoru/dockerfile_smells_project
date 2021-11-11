FROM debian:latest
MAINTAINER Sam Mulube <sam@umbrellium.co.uk>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  make \
  python-pip \
  python-dev \
  texlive texlive-latex-recommended \
  texlive-latex-extra \
  texlive-fonts-recommended

RUN pip install Sphinx==1.4.4 sphinx_rtd_theme alabaster sphinx_bootstrap_theme

CMD ["/bin/bash"]

WORKDIR /doc
