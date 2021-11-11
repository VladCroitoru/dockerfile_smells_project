FROM jupyter/datascience-notebook

USER root

# Install conda packages
RUN conda update --all --no-channel-priority --yes && conda install joblib libxgboost py-xgboost -y && conda install tqdm plotly xlwt xlsxwriter -c conda-forge -y

# TensorFlow
RUN pip3 install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.2.1-cp36-cp36m-linux_x86_64.whl

USER $NB_USER
