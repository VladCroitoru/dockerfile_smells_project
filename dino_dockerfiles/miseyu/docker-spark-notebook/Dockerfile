FROM miseyu/docker-spark-streaming

# Pip
RUN apt-get -y update && \
    apt-get -y install python3-pip && \
    pip3 install --upgrade pip

# Notebook
RUN pip --no-cache-dir install jupyter
COPY ./toree-0.2.0.dev1.tar.gz /tmp/
RUN pip --no-cache-dir install /tmp/toree-0.2.0.dev1.tar.gz && \
    jupyter toree install

EXPOSE 8888
