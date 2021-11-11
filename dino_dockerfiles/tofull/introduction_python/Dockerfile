FROM python:3

ADD *.ipynb /notebooks/
ADD notre_premier_module /notebooks/notre_premier_module/
ADD requirements.txt /notebooks/
ADD un_module_elementaire.py /notebooks/
ADD data /notebooks/data/
ADD assets /notebooks/assets/

RUN pip install jupyter
RUN pip install RISE
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter-nbextension enable rise --py --sys-prefix

RUN pip install -r /notebooks/requirements.txt

ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--notebook-dir=/notebooks/", "--NotebookApp.token=''"]