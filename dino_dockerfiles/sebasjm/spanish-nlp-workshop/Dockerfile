FROM continuumio/anaconda3

MAINTAINER Sebastian Marchano <sebasjm@gmail.com>

RUN mkdir /opt/notebooks
RUN mkdir /root/.jupyter
WORKDIR /opt/notebooks

RUN conda config --add channels conda-forge && \
    conda create -y -n nlp python=3 gensim spacy matplotlib scikit-learn pandas ipykernel && \
    apt-get update --fix-missing && apt-get install -y libgomp1 unzip python3-pip

RUN /bin/bash -c "source activate nlp; python3 -m pip install bs4 && python3 -m spacy download es && /opt/conda/bin/conda install jupyter -y --quiet && python3 -m ipykernel install --user"

COPY start.sh /start.sh
COPY jupyter_notebook_config.py /root/.jupyter
COPY src/spanish-nlp.ipynb /opt/notebooks

EXPOSE 8888

CMD ["/bin/bash","/start.sh"]
