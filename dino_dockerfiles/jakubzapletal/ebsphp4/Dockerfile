FROM jakubzapletal/ebsphp1:5.5

RUN \
    apt-get update \
    && apt-get install -y --force-yes --no-install-recommends \
        python-pip \
    && rm -rf /var/lib/apt/lists/* \
    && pip install supervisor
