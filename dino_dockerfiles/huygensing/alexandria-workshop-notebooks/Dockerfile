FROM jupyter/datascience-notebook
# user is set to jovyan

USER root
ENV vol=/data
RUN apt-get update \
  && apt-get install -y graphviz \
  && mkdir -p ${vol}/examples/data \
  && mkdir -p ${vol}/work \
  && chown -R jovyan ${vol}
COPY *.ipynb ${vol}/examples/
COPY data/* ${vol}/examples/data/

ENV tmp=/tmp
ADD . ${tmp}
WORKDIR ${tmp}
USER jovyan
RUN pip install --user pydot \
  && python setup.py install --user \
  && git clone https://github.com/HuygensING/alexandria-markup-python-client.git \
  && cd alexandria-markup-python-client \
  && python setup.py install --user

WORKDIR ${vol}

EXPOSE 8888
ENTRYPOINT start-notebook.sh --NotebookApp.token=''
VOLUME ${vol}/work
