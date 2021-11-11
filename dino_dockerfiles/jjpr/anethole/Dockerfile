FROM python:3.8

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y  --no-install-recommends \
    build-essential \
    git \
    wget

RUN apt update && \
    apt install -y  --no-install-recommends \
    xvfb \
    x11-utils \
    libx11-dev \
    qt5-default

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash

RUN apt update && \
    apt install -y  --no-install-recommends \
    nodejs

RUN npm install -g npm

RUN apt clean

RUN pip install matplotlib

RUN pip install numpy

RUN pip install pandas

RUN pip install scipy

RUN pip install sympy

RUN pip install jupyterlab

RUN pip install mayavi

RUN pip install ipyevents

RUN pip install Pillow

RUN pip install xvfbwrapper

RUN pip install pymeshlab

RUN jupyter nbextension install mayavi --py --sys-prefix
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager ipyevents

ENV DISPLAY :99

RUN mkdir -p /data/notebooks
RUN mkdir -p /data/tools
RUN mkdir -p /data/examples/images

COPY Equation_To_Object_Instructions.ipynb /data/examples/
COPY images/ruffle_equation.png /data/examples/images/
COPY images/wrapped_ruffle.png /data/examples/images/
COPY images/printed.png /data/examples/images/
COPY images/saddle_grapher.png /data/examples/images/

ENV SHELL=/bin/bash

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--notebook-dir=/data"]
