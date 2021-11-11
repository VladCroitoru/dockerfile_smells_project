FROM centos:7

LABEL maintainer="teake.nutma@gmail.com"
LABEL description="Builds linux-64 conda packages. CentOS 7 + miniconda + conda-build."

# Configuration options.
ARG CONDA_PREFIX=/opt/conda

# Set a UTF-8 locale. Useful for running Python 3 programs.
ENV LANG en_US.utf-8
ENV LC_ALL en_US.utf-8

# Fetch updates and install dependencies.
# bzip2 is required for installing conda.
# git and openssh-clients are required for cloning git repositories in recipes.
# patch is required for applying patches in recipes.
RUN yum -y update \
    && yum -y install bzip2 git openssh-clients patch \
    && yum clean all \
    && rm -rf /var/cache/yum

# Install the latest Miniconda with Python 3 and update everything.
RUN curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh \
    && sh miniconda.sh -b -p ${CONDA_PREFIX} \
    && rm miniconda.sh \
    && ${CONDA_PREFIX}/bin/conda config --set show_channel_urls True \
    && ${CONDA_PREFIX}/bin/conda config --set path_conflict prevent \
    && ${CONDA_PREFIX}/bin/conda config --set notify_outdated_conda false \
    && ${CONDA_PREFIX}/bin/conda update -c conda-forge --yes --all \
    && ${CONDA_PREFIX}/bin/conda install -c conda-forge --yes conda-build conda-verify coverage coverage-fixpaths \
    && ${CONDA_PREFIX}/bin/conda clean -tipy \
    && ${CONDA_PREFIX}/bin/conda-build purge-all \
    # conda init wants to edit ~/.bashrc, but if that doesn't exist it fails.
    && touch ~/.bashrc \
    && ${CONDA_PREFIX}/bin/conda init bash

# Add a shell script that activates conda ...
COPY entrypoint.sh /opt/docker/bin/entrypoint.sh
# ... and make it the Docker entrypoint so that conda is available when we run a container.
ENTRYPOINT [ "/bin/bash", "/opt/docker/bin/entrypoint.sh" ]
# Provide a default command (`bash`), which will start if the user doesn't specify one.
CMD [ "/bin/bash" ]
