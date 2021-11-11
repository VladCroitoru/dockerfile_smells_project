from continuumio/miniconda:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN conda install --yes Matplotlib

ONBUILD COPY requirements.txt /usr/src/app/

ONBUILD RUN pip install --no-cache-dir -r requirements.txt

ONBUILD COPY . /usr/src/app
