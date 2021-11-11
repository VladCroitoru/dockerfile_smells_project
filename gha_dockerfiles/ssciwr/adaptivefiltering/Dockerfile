FROM jupyter/base-notebook:396024a4ddc1

# Copy the repository into the container
COPY --chown=${NB_UID} . /opt/adaptivefiltering

# Install Conda environment
RUN conda env update -n base --file /opt/adaptivefiltering/environment.yml && \
    conda clean -a -q -y

# Build and install the project
RUN conda run -n base python -m pip install /opt/adaptivefiltering

# Make JupyterLab the default for this application
ENV JUPYTER_ENABLE_LAB=yes

# Copy all the notebook files into the home directory
RUN rm -rf ${HOME}/work && \
    cp /opt/adaptivefiltering/jupyter/* ${HOME}

# Remove the redundant data from /opt/adaptivefiltering
RUN rm -rf /opt/adaptivefiltering/*
