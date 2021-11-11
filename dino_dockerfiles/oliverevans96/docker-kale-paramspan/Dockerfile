FROM oliverevans96/jupyterlab-widgets

RUN conda install qgrid=1.0.2 dill=0.2.7.1
RUN pip install arctic==1.65.0
RUN jupyter labextension install qgrid@1.0.2

COPY ParamSpan.ipynb /home/jovyan

