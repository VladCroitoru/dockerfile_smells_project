##### Shared Environment stage #########################################################
FROM registry.hub.docker.com/library/python:3.7-slim AS base

ENV PIP_DEPENDENCIES wheel pipenv
ENV TICKIT_DIR /tickit

# Install pip dependencies
RUN rm -rf /usr/bin/python3.9
RUN python3.7 -m pip install --upgrade pip
RUN python3.7 -m pip install ${PIP_DEPENDENCIES}

# Copy tickit code into container
COPY . ${TICKIT_DIR}
WORKDIR ${TICKIT_DIR}

RUN pipenv install --python python3.7 --system --deploy

##### Runtime Stage ####################################################################
FROM registry.hub.docker.com/library/python:3.7-slim AS runtime

ENV TICKIT_DIR /tickit
WORKDIR ${TICKIT_DIR}

ENV PYTHON_SITE_PACKAGES /usr/local/lib/python3.7/site-packages

COPY --from=base ${PYTHON_SITE_PACKAGES} ${PYTHON_SITE_PACKAGES}
COPY . ${TICKIT_DIR}

RUN python3.7 -m pip install tickit

CMD ["python3.7", "-m", "tickit"]

##### Developer Base Stage #############################################################
FROM base AS base_dev

RUN pipenv install --python python3.7 --system --deploy --dev

##### Developer Stage ##################################################################
FROM registry.hub.docker.com/library/python:3.7-slim AS developer

ENV TICKIT_DIR /tickit
WORKDIR ${TICKIT_DIR}

ENV PYTHON_SITE_PACKAGES /usr/local/lib/python3.7/site-packages

COPY --from=base_dev ${PYTHON_SITE_PACKAGES} ${PYTHON_SITE_PACKAGES}
COPY . ${TICKIT_DIR}

RUN python3.7 -m pip install tickit

CMD ["python3.7", "-m", "tickit"]
