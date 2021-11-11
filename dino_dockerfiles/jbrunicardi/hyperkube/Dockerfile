FROM quay.io/coreos/hyperkube:v1.2.2_coreos.0

RUN set -x \
    && apt-get update --quiet \
    && apt-get upgrade --quiet --yes \
    && apt-get install --quiet --yes --no-install-recommends nfs-common \
    && apt-get autoremove --yes \
    && apt-get clean