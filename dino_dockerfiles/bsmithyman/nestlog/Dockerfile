FROM continuumio/miniconda:py27_latest

MAINTAINER Brendan Smithyman

RUN DEBIAN_FRONTEND="noninteractive" apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y upgrade
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install git
RUN /opt/anaconda/bin/conda update --prefix /opt/anaconda conda
RUN /opt/anaconda/bin/conda install pip pymongo
RUN /opt/anaconda/bin/pip install schedule
RUN /opt/anaconda/bin/pip install plotly
RUN /opt/anaconda/bin/pip install git+https://github.com/bsmithyman/nest_thermostat.git

ADD nestlog.py /nestlog.py
ADD plotresults.py /plotresults.py

CMD /nestlog.py