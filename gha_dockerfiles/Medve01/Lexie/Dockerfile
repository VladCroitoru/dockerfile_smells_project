FROM ubuntu:focal

SHELL ["/bin/bash", "-xe", "-c"]

ARG DEBIAN_FRONTEND=noninteractive

COPY . /lexie
WORKDIR /lexie

RUN apt-get update -q \
 && apt-get install -y -q --no-install-recommends \
        python3-wheel \
        python3-pip \
        gunicorn \
 && if [ -e requirements.txt ]; then \
        python3 -m pip install --no-cache-dir --disable-pip-version-check \
            -r requirements.txt; \
    fi \
 && python3 -m pip install \
        --no-cache-dir --disable-pip-version-check \
        /lexie/ \
 && apt-get remove -y python3-pip python3-wheel \
 && apt-get autoremove -y \
 && apt-get clean -y \
 && rm -rf /var/lib/apt/lists/* \
 && useradd _gunicorn --no-create-home --user-group

USER _gunicorn

CMD ["gunicorn", \
     "--bind", "0.0.0.0:8000", \
     "lexie_app"]