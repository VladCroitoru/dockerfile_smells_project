# download base image ubuntu 20.04
FROM ubuntu:20.04
LABEL maintainer="Till S. Witt <mail@tillwitt.de>"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y

# Install PIP
RUN apt-get -y install python3-pip

# Latex/PDF support for Sphinx-docs
RUN apt-get -y install \
  latexmk \
  texlive-fonts-recommended \
  texlive-lang-english \
  texlive-lang-french \
  texlive-lang-german \
  texlive-latex-extra \
  texlive-latex-recommended

# install tooling
RUN apt-get -y install \
  inotify-tools \
  wget

# PlantUML tooling
RUN apt-get -y install \
  default-jre \
  graphviz

# Install pip components
RUN pip3 install --upgrade \
  pip \
  recommonmark \
  sphinx-rtd-theme \
  sphinxcontrib-needs \
  sphinxcontrib-plantuml

# make plantuml executable
ADD tools/plantuml /usr/local/bin/
RUN chmod +x /usr/local/bin/plantuml

# adds a local file to the image
ADD /tools/runAfterBoot.sh /tools/
RUN chmod 755 /tools/runAfterBoot.sh
ADD /tools/watch.sh /tools/
RUN chmod 755 /tools/watch.sh

WORKDIR /tools
ADD /tools/plantuml.1.2017.19.jar .

# make root project folder writable to any UID
RUN mkdir /project \
  && chmod 777 /project

WORKDIR /project

# starting the command line
ENTRYPOINT /tools/runAfterBoot.sh
