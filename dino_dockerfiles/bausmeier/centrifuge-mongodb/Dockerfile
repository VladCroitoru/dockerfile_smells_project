FROM bausmeier/centrifuge:latest

USER root
ADD . /src
RUN cd /src && \
    python setup.py install && \
    rm -r /src

USER centrifuge
ENV PYTHON_EGG_CACHE /data
ENV CENTRIFUGE_STORAGE centrifuge_mongodb.Storage
