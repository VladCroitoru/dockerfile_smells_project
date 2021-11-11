FROM jupyter/scipy-notebook:latest
MAINTAINER Kirill Morozov <kir.morozov@gmail.com>

USER root
RUN apt-get update && \
    apt-get upgrade --yes && \
    apt-get install --yes mc git make cmake build-essential libboost-all-dev libstdc++6 ssh-client ssh sshpass python-dev libmysqlclient-dev

USER $NB_USER

RUN conda install --quiet --yes pip setuptools && \
    conda install --quiet --yes -n python2  pip setuptools
#RUN cd ~ && \
#    git clone --branch=master https://github.com/bigartm/bigartm.git && \
#    cd bigartm && \
#    mkdir build && cd build && \
#    cmake -Wno-dev .. && make && \
#    PATH=/opt/conda/envs/python2/bin:$PATH make && \
#    cd ~/bigartm/3rdparty/protobuf-3.0.0/python && \
#    python setup.py install && \
#    /opt/conda/envs/python2/bin/python setup.py install && \
#    cd ~/bigartm/python && \
#    python setup.py install && \
#    /opt/conda/envs/python2/bin/python setup.py install
#
#ENV ARTM_SHARED_LIBRARY /home/jovyan/bigartm/build/src/artm/libartm.so

RUN conda install --quiet --yes gensim pandas-datareader plotly && \
    conda install --quiet --yes -n python2 gensim pandas-datareader plotly mysql-python

RUN ln -sfn /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /opt/conda/envs/python2/lib/libstdc++.so && \
    ln -sfn /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /opt/conda/envs/python2/lib/libstdc++.so.6

RUN pip install nbimporter jupyter_contrib_nbextensions mysqlclient cufflinks && \
    pip install --pre -U statsmodels && \
    PATH=/opt/conda/envs/python2/bin:$PATH pip install nbimporter jupyter_contrib_nbextensions cufflinks && \
    PATH=/opt/conda/envs/python2/bin:$PATH pip install --pre -U statsmodels 

