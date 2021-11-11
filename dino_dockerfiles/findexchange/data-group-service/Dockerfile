FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update \
 && apt-get install \
        libatlas-dev \
        libatlas-base-dev \
        liblapack-dev \
        gfortran \
        --assume-yes \
        --no-install-recommends \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#RUN wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh && \
#    bash miniconda.sh -b -p $HOME/miniconda && \
#    export PATH="$HOME/miniconda/bin:$PATH" && \
#    conda update --yes conda
#
#RUN conda install --yes python=2.7 pip numpy scipy pandas

COPY requirements_docker.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /usr/src/app/src
EXPOSE 5000

COPY setup.py /usr/src/app/setup.py
RUN python /usr/src/app/setup.py build_ext -i

CMD ["python", "src/flask_app.py"]
