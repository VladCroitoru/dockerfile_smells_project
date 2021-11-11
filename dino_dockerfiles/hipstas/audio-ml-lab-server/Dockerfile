# Audio ML Notebook Server

FROM hipstas/audio-ml-lab
MAINTAINER Steve McLaughlin <stephen.mclaughlin@utexas.edu>

EXPOSE 8887
ENV PYTHONWARNINGS="ignore:a true SSLContext object"

CMD jupyter notebook --ip 0.0.0.0 --port 8887 --no-browser --allow-root --NotebookApp.iopub_data_rate_limit=1.0e10
