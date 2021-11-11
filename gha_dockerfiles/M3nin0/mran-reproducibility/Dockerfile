FROM jupyter/base-notebook:lab-3.1.13

#
# 1. Configuring the base dependencies
#
USER root
RUN apt-get update -y \
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

#
# 2. Install the dependencies
#
COPY . build

RUN cd build \
   && conda env update --file environment.yml --prune

#
# 3. Changing the user
#
RUN chown -R ${NB_UID} /home/jovyan/

USER ${NB_USER}
