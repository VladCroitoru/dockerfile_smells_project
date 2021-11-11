FROM jupyter/datascience-notebook

RUN git clone https://github.com/ccc1685/covid-19
WORKDIR covid-19

RUN pip install -e .
RUN python scripts/get-data.py
RUN python scripts/run.py nonlinearmodel
RUN python scripts/visualize.py
RUN python scripts/make-tables.py
