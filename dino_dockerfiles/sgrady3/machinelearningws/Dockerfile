FROM jupyter/tensorflow-notebook

USER $NB_USER

# Python packages from conda
RUN conda install --quiet --yes \
    -c conda-forge python-graphviz &&\
    conda clean -tipsy && \
fix-permissions $CONDA_DIR

RUN mkdir Workspace && mkdir Results && mkdir Results/Hierarchical_Clustering && mkdir Results/Decision_Tree && mkdir Results/Neural_Networks
COPY ./Workspace Workspace

USER $NB_USER

