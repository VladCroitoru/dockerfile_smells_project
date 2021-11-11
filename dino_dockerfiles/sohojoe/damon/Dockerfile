FROM continuumio/miniconda
MAINTAINER Joe Booth "joe@joebooth.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# copy damon to python packages
COPY damon1 PYTHONPATH

# install depenadcies
WORKDIR /damon_install
ADD ./requirements.txt /damon_install/requirements.txt
RUN pip install -r requirements.txt

# test damon is in path
RUN python -c "import site; site.getsitepackages()" 

