# Use SKA python image as base image
FROM nexus.engageska-portugal.pt/ska-tango-images/pytango-builder:9.3.3.3 AS buildenv
FROM nexus.engageska-portugal.pt/ska-tango-images/pytango-runtime:9.3.3.3 AS runtime

ARG IMAGE_VERSION=0.0.1

LABEL \
      author="SKA India and SARAO and CSIRO and INAF" \
      description="A set of generic base devices for SKA Telescope" \
      license="BSD-3-Clause" \
      registry="nexus.engageska-portugal.pt/ska-telescope/ska_tango_base" \
      vendor="SKA Telescope" \
      org.skatelescope.team="NCRA, Karoo, MCCS, CREAM" \
      org.skatelescope.version="${IMAGE_VERSION}" \
      org.skatelescope.website="https://gitlab.com/ska-telescope/ska-tango-base/"

# create ipython profile to so that itango doesn't fail if ipython hasn't run yet
RUN ipython profile create

# Note: working dir is `/app` which will have a copy of our repo
# The pip install will be a "user installation" so update path to access console scripts
ENV PATH=/home/tango/.local/bin:$PATH
RUN python3 -m pip install -e . --user
CMD ["SKABaseDevice"]
