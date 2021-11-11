FROM tensorflow/tensorflow:latest-gpu

RUN pip install --upgrade pip
RUN pip install tensorflow
RUN pip install scipy
RUN pip install numpy
RUN pip install matplotlib
RUN pip install notebook
RUN pip install statsmodels
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install seaborn
RUN pip install jupyter
RUN pip install opencv-python

RUN mkdir project && chown -R 1000:1000 project
WORKDIR project

RUN export PYTHONPATH=$PYTHONPATH:/project/src

RUN mkdir notebooks
WORKDIR notebooks

RUN mkdir /.local && chown -R 1000:1000 /.local

USER 1000:1000

ENTRYPOINT jupyter notebook --no-browser --ip 0.0.0.0 --port 8888