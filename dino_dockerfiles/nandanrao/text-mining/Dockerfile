FROM jupyter/datascience-notebook

USER $NB_USER

RUN conda install --quiet --yes -c conda-forge spacy && \
    conda install --quiet --yes -c anaconda nltk

RUN pip install --quiet langdetect lightgbm

RUN python -m spacy download en_core_web_md && \
    python -m spacy download es_core_news_md && \
    python -m spacy download es && \
    python -m spacy download en

COPY utils.py /home/jovyan/utils.py
COPY migrants.ipynb /home/jovyan/migrants.ipynb
COPY kaggle /home/jovyan/kaggle
