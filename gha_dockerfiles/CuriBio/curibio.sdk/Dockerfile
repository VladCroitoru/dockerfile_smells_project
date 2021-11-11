# For use in mybinder.org Jupyter notebooks
FROM python:3.9.2-slim-buster
# install the notebook package # Eli (9/10/20): no known reason for those specific versions of pip/notebook. Just pinning it for good practice
RUN pip install --no-cache --upgrade pip==21.0.1 && \
    pip install --no-cache --upgrade notebook==6.2.0 && \
    pip install --no-cache --upgrade jupyterlab==3.0.9

RUN pip install curibio.sdk --no-cache

# create user with a home directory
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}


RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

# copy files from cloned repo into the HOME directory
# chown flag is necessary to make sure that the Notebooks don't launch as "read only" mode (without chown they are still owned by the 'root' user)
COPY --chown=${NB_USER}:${NB_USER} . ${HOME}/repo
# COPY notebooks/ ${HOME} # to make it simpler for the users, just copy the notebooks folder right into the main Home directory. The URL links point to the file struction in the Home directory, so make sure to adjust those accordingly
# COPY tests/h5/v0.3.1/MA201110001__2020_09_03_213024/ ${HOME}/test-data

WORKDIR ${HOME}
USER ${USER}

# Eli (9/16/20): for some reason Docker is giving weird errors attempting to copy directly into the folders, so using Unix commands to move the files to where they're needed and delete the unneeded files
# clear out the unneeded files copied from the repo
RUN cp repo/notebooks/*.ipynb . && \
    mkdir sample-data && \
    mkdir my-data && \
    cp repo/tests/h5/v0.3.1/MA201110001__2020_09_03_213024/*.h5 ./sample-data && \
    rm -r repo
