# Linux OS
FROM jupyter/base-notebook

# Maintener
MAINTAINER zorino <maximilien1er@gmail.com>

USER root

# Install dependencies for XGBoost and TensorFlow
RUN apt-get update -y && apt-get install -y git-core build-essential curl libfreetype6-dev libxft-dev libgomp1 python-matplotlib  \
 && curl https://bootstrap.pypa.io/ez_setup.py -o - | python

USER $NB_USER

# Install python2 ipykernel in conda env.
RUN conda create -n ipykernel_py2 python=2 ipykernel
ENV PY2_PATH=/opt/conda/envs/ipykernel_py2/bin/
RUN $PY2_PATH/python2 -m ipykernel install --user

# Install Numpy, Scipy, Sk-learn, Pandas, Keras, Seaborn, Statsmodels
RUN pip install numpy scipy scikit-learn pandas keras tqdm seaborn statsmodels
RUN $PY2_PATH/pip install numpy scipy scikit-learn pandas keras tqdm seaborn statsmodels

# Install TensorFlow
RUN export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp35-cp35m-linux_x86_64.whl \
 && pip install --upgrade $TF_BINARY_URL
 # && $PY2_PATH/pip install --upgrade $TF_BINARY_URL

USER root

# Install XGBoost
RUN cd /opt \
 && git clone --recursive https://github.com/dmlc/xgboost \
 && cd xgboost && make -j 2 && cd python-package \
 && python setup.py install
 # && $PY2_PATH/python2 setup.py install

# Clean-up
RUN rm -fr /home/$NB_USER/work/* \
 && apt-get purge -y build-essential curl git-core \
 && apt-get autoremove -y \
 && apt-get clean all

USER $NB_USER

ENV KERAS_BACKEND tensorflow

CMD ["start-notebook.sh"]
