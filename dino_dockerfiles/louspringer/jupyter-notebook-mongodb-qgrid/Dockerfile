FROM jupyter/datascience-notebook

USER root

RUN conda config --system --append channels r && \
    conda install --quiet --yes \
    pymongo \
    openpyxl

RUN conda install --quiet --yes  \
	-c tim_shawver/label/dev qgrid==1.0.0b8