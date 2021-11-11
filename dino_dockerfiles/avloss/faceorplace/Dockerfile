FROM debian:stable
MAINTAINER Anton Loss @avloss

USER root

RUN apt-get update && apt-get install -y wget bzip2 git unzip

RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh \
    && bash Miniconda2-latest-Linux-x86_64.sh -b -p /anaconda2 \
    && rm Miniconda2-latest-Linux-x86_64.sh
RUN /anaconda2/bin/conda install Flask==0.12.2 \
    matplotlib==2.0.0 numpy==1.12.0 Pillow==4.2.1 \
    python-dateutil==2.6.0 six==1.10.0 \
    waitress==1.0.2 Werkzeug==0.12.2
RUN /anaconda2/bin/pip install tensorflow==1.2.1

COPY faceorplace /faceorplace

EXPOSE 8080

CMD /anaconda2/bin/python faceorplace/server.py