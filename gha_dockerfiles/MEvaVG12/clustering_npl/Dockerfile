FROM continuumio/anaconda3
SHELL ["/bin/bash", "-c"]
WORKDIR /opt/notebooks/clustering

COPY ./src/requirements.txt /tmp/requirements.txt/

RUN conda create --name keras python=3.5
RUN conda init bash
RUN source activate keras
RUN echo pwd
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN pip install pyLDAvis
RUN python -m spacy download es_core_news_sm

RUN conda install -c conda-forge keras
RUN conda install -c conda-forge wordcloud=1.6.0
RUN pip install --upgrade gensim
# Setup for Jupyter Notebook
RUN groupadd -g 1000 jupyter && \
useradd -g jupyter -m -s /bin/bash jupyter && \
echo "jupyter:jupyter" | chpasswd && \
/opt/conda/bin/conda clean -y --all

COPY entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/entrypoint.sh
EXPOSE 8888
USER jupyter

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD []