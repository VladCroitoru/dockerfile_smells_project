# basic python3 image as base
FROM harbor.vantage6.ai/algorithms/algorithm-base

# This is a placeholder that should be overloaded by invoking
# docker build with '--build-arg PKG_NAME=...'
ARG PKG_NAME="v6_summary_omop"

# Required for the psycopg2 dependency
RUN apt-get update
RUN apt-get install -y apt-utils gcc libpq-dev

# install federated algorithm
COPY . /app
RUN pip install /app

ENV PKG_NAME=${PKG_NAME}

# Tell docker to execute `docker_wrapper()` when the image is run.
CMD python -c "from v6_summary_omop.docker_wrapper import docker_wrapper; docker_wrapper('${PKG_NAME}')"
