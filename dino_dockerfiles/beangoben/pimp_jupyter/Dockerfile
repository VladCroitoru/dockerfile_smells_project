FROM  jupyter/scipy-notebook

# make bash default shell
USER root
RUN ln -snf /bin/bash /bin/sh

RUN apt-get update && \
    apt-get install -y jq && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN conda install -y -q conda-build xlrd xlwt &&\
    conda update -y -q notebook numpy scipy matplotlib seaborn ipython && \
    conda clean --all

#jupyter theme selector
RUN mkdir /opt/conda/share/jupyter/nbextensions/jupyter_themes &&\
    wget https://raw.githubusercontent.com/merqurio/jupyter_themes/master/theme_selector.js &&\
    mv theme_selector.js /opt/conda/share/jupyter/nbextensions/jupyter_themes &&\
    jupyter nbextension enable jupyter_themes/theme_selector

# live reveal
RUN conda install -y -q -c damianavila82 rise

# jupyter notebook extensions
#RUN conda install -y -q -c conda-forge jupyter_contrib_nbextensions yapf xlrd xlwt && \
#    conda clean --all && \
RUN pip install --upgrade --ignore-installed https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master yapf xlrd xlwt

RUN conda install -y -q -c conda-forge -n python2 yapf xlrd xlwt && \
    conda clean --all

#RUN conda install -y jupyter_nbextensions_configurator psutil
RUN jupyter nbextensions_configurator enable --system && \
    jupyter contrib nbextension install --system
# update conda
RUN chown -R $NB_USER /home/$NB_USER
USER $NB_USER

RUN jupyter nbextension enable code_font_size/code_font_size && \
    jupyter nbextension enable ruler/main  && \
    jupyter nbextension enable table_beautifier/main && \
    jupyter nbextension enable toggle_all_line_numbers/main && \
    jupyter nbextension enable code_prettify/code_prettify && \
    jupyter nbextension enable toc2/main && \
    jupyter nbextension enable limit_output/main && \
    jupyter nbextension enable execute_time/ExecuteTime

# load default extension options
COPY nbextensions_default.json /home/$NB_USER/.jupyter/nbconfig
RUN cd /home/$NB_USER/.jupyter/nbconfig && jq -s add notebook.json nbextensions_default.json > new.json && mv new.json notebook.json
#jupyter css
RUN mkdir -p /home/$NB_USER/.jupyter/custom
COPY custom /home/$NB_USER/.jupyter/custom
