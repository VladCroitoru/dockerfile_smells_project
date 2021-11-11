FROM tensorflow/tensorflow:nightly-gpu-py3
MAINTAINER Sam Lee <misgod.tw@gmail.com>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ENV KERAS_BACKEND tensorflow

RUN pip install keras seaborn scikit-learn scikit-image pandas xgboost pillow h5py

# Set up our notebook config.
COPY jupyter_notebook_config.py /root/.jupyter/


# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /


# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

VOLUME /notebooks
WORKDIR "/notebooks"


CMD ["/run_jupyter.sh"]
