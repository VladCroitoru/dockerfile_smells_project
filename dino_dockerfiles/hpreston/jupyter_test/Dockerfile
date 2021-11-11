FROM python:3.6.2-jessie
MAINTAINER Hank Preston <hank.preston@gmail.com>
EXPOSE 8888

# Install build requirements
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    build-essential \
    unzip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Download and install ACI Toolkit
RUN cd /tmp && \
  wget https://github.com/datacenter/acitoolkit/archive/master.zip && \
  unzip master.zip && \
  cd acitoolkit-master && \
  python setup.py install

# Install jupyter
RUN pip install jupyter

# Prep local directory for storing notebooks
RUN mkdir /notebook
WORKDIR /notebook

# Copy in notebook files to start with
COPY *.ipynb /notebook/

# Start Jupyter
CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root" ]
