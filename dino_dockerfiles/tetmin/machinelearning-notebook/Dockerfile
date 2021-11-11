FROM jupyter/datascience-notebook

RUN conda install -c conda-forge tensorflow

# install in the default python3 environment
RUN pip install keras geoip2

# install in the python2 environment also
RUN bash -c "source activate python2 && pip install keras geoip2"

EXPOSE 6006
