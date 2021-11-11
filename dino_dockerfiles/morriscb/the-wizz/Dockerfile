FROM jupyter/scipy-notebook:latest

MAINTAINER Christopher Morrison "morrison.chrisb@gmail.com"

RUN pip install pyarrow && \
    pip install astropy

USER root

USER $NB_UID
WORKDIR $HOME/work

RUN git clone https://github.com/morriscb/the-wizz.git
WORKDIR $HOME/work/the-wizz
RUN git checkout u/morriscb/python-only && \
    python setup.py install --user

WORKDIR $HOME/work
