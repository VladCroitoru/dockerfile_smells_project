FROM avikdatta/basejupyterdockerimage

MAINTAINER reach4avik@yahoo.com

ENTRYPOINT []

ENV NB_USER vmuser

USER root
WORKDIR /root/

RUN apt-get -y update &&   \
    apt-get install --no-install-recommends -y   \
    tk-dev                 \
    gfortran               \
    sqlite3                \
    libhdf5-serial-dev     \
    libigraph0-dev         \
    &&  apt-get purge -y --auto-remove \
    &&  apt-get clean \
    &&  rm -rf /var/lib/apt/lists/*
    
USER $NB_USER
WORKDIR /home/$NB_USER

ENV PYENV_ROOT /home/$NB_USER/.pyenv
ENV PATH "$PYENV_ROOT/libexec/:$PATH" 
ENV PATH "$PYENV_ROOT/shims/:$PATH"

RUN eval "$(pyenv init -)" 
RUN pyenv global 3.5.2

#RUN wget https://nodejs.org/dist/v8.11.1/node-v8.11.1-linux-x64.tar.xz \
#    && tar -xvf node-v8.11.1-linux-x64.tar.xz

#ENV PATH="/home/$NB_USER/node-v8.11.1-linux-x64/bin:$PATH"

#RUN mkdir -p /home/$NB_USER/tmp    \
#    && npm install --global yarn   \
#    && git clone https://github.com/jupyterlab/jupyter-renderers.git \
#    && cd jupyter-renderers        \
#    && jlpm                        \
#    && jlpm build                  \
#    && jupyter labextension link packages/plotly-extension \
#    && jlpm build                  \
#    && jupyter labextension link packages/fasta-extension  \
#    && jlpm build                  \
#    && jupyter lab build           \
#    && rm -rf /home/$NB_USER/tmp   \
#    && mkdir -p /home/$NB_USER/tmp 
          
RUN pip install    \
        --no-cache-dir -q \
        cython     \
        numpy      \
        scipy      \
        sklearn    \
        pandas     \
        matplotlib \
        seaborn    \
        pandas_datareader  \
        bs4        \
        matplotlib \
        nltk       \
        gensim     \
        pymysql    \
        xlrd       \
        openpyxl   \
        sqlalchemy \
        slackclient \
        asana       \
        holoviews   \
        bokeh       \
        line_profiler \
        memory_profiler \
        plotly        \
        cufflinks     \
        python-igraph \
        louvain       

WORKDIR /home/$NB_USER

RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension

RUN set -ex; \
    rm -rf /home/$NB_USER/.cache; \
    find $PYENV_ROOT -type d -a \( -name test -o -name tests \) -exec rm -rf '{}' +; \
    find $PYENV_ROOT -type f -a \( -name '*.pyc' -o -name '*.pyo' \) -exec rm -f '{}' +; \
    rm -rf /home/$NB_USER/tmp; \
    mkdir /home/$NB_USER/tmp
#    rm -rf node-v8.11.1-linux-x64.tar.xz node-v8.11.1-linux-x64 jupyter-renderers; \
    
    
EXPOSE 8888
CMD ["jupyter","lab","--ip=0.0.0.0","--port=8888","--no-browser","--NotebookApp.iopub_data_rate_limit=100000000"]
