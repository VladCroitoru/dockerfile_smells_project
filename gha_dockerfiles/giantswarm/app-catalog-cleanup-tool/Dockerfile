FROM python:3.9.7-slim AS base

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    ACCT_DIR="/acct" \
    PIPENV_VER="2021.5.29"

RUN pip install --no-cache-dir pipenv==${PIPENV_VER}

WORKDIR $ACCT_DIR


FROM base as builder

# pip prerequesties
RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY Pipfile Pipfile.lock ./

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --clear


FROM base

ENV USE_UID=0 \
    USE_GID=0 \
    PATH="${ACCT_DIR}/.venv/bin:$PATH" \
    PYTHONPATH=$ACCT_DIR

# install dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y sudo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder ${ACCT_DIR}/.venv ${ACCT_DIR}/.venv

COPY app_catalog_cleanup_tool/ ${ACCT_DIR}/app_catalog_cleanup_tool/

COPY container-entrypoint.sh /usr/bin
RUN chmod +x /usr/bin/container-entrypoint.sh

WORKDIR $ACCT_DIR/workdir

# we assume the user will be using UID==1000 and GID=1000; if that's not true, we'll run `chown`
# in the container's startup script
RUN chown -R 1000:1000 $ACCT_DIR

ENTRYPOINT ["container-entrypoint.sh"]

CMD ["-h"]
