FROM jupyter/datascience-notebook

ENV CALITP_SERVICE_KEY_PATH=/home/jovyan/warehouse_key.json

RUN pip install \
    git+https://github.com/machow/siuba.git@stable \
    calitp==0.0.8 \
    intake==0.6.4 \
    intake-dcat==0.4.0 \
    intake-geopandas==0.3.0 \
    intake-parquet==0.2.3
