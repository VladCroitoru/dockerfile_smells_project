FROM ubuntu:focal

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y -q python3-pip texlive texlive-latex-extra git-all doxygen graphviz cmake doxyqml librsvg2-bin locales && pip3 install boto3 awscli sphinx==3.0.4

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN mkdir documents
WORKDIR /documents
VOLUME /documents

CMD ["/bin/bash"]
