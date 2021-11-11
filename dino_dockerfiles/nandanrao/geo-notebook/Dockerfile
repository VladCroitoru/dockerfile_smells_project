FROM jupyter/datascience-notebook

USER $NB_USER

RUN conda create --quiet --yes -n geopandas python=2.7 \
    'geopandas' \
    'ipykernel' \
    'boto3'

ENV PATH /opt/conda/envs/geopandas/bin:$PATH

RUN python -m ipykernel install --user --name geopandas --display-name "Python (geopandas)"

