FROM continuumio/miniconda3:4.8.2

ENV PYTHONUNBUFFERED 0

RUN apt-get update && apt-get -y install \
    libgl1-mesa-glx

ADD ./environment.yml /tmp
RUN conda env create -f /tmp/environment.yml

# alternative to `source activate glia`
ENV PATH /opt/conda/envs/glia/bin:$PATH

# build matplotlib font cache
RUN python -c 'import matplotlib.pyplot'

ADD ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

ADD . /src
WORKDIR /src
RUN python setup.py develop
ENTRYPOINT ["glia"]
