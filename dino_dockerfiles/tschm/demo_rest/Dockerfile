# Set the base image to Ubuntu
FROM continuumio/miniconda3

RUN conda install -q -y pandas requests

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@gmail.com"

ADD ./config /pyrest/config
ADD ./pyserver /pyrest/pyserver
ADD ./start.py /pyrest/start.py

EXPOSE 8000

# install Python environment
RUN pip install waitress flask-restful

CMD python /pyrest/start.py
