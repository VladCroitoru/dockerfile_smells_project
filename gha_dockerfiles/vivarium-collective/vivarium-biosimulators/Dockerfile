# BioSimulator dockerfiles can be found here: https://github.com/biosimulators/Biosimulators
# set base image
FROM ghcr.io/biosimulators/biosimulators

# LABEL \
#     org.opencontainers.image.title="Vivarium-BioSimulators Jupyter server" \
#     org.opencontainers.image.url="https://github.com/vivarium-collective/vivarium-biosimulators" \
#     org.opencontainers.image.documentation="https://vivarium-core.readthedocs.io/en/latest/" \
#     org.opencontainers.image.source="https://github.com/vivarium-collective/vivarium-biosimulators"" \
#     org.opencontainers.image.authors="BioSimulators & Vivarium Team" \
#     org.opencontainers.image.vendor="BioSimulators & Vivarium Team"

# copy vivarium-simulators to working dir
COPY . /app

# install dependencies
## biosimulators test suite for examples
RUN git clone https://github.com/biosimulators/Biosimulators_test_suite.git
RUN pip install Biosimulators_test_suite

## vivarium-biosimulators requirements
RUN pip install -e .
RUN pip install -r requirements.txt
RUN pip install -r update_requirements.txt --upgrade

# start mock up server for output
# RUN pipenv run xvfb-startup.sh

# command
CMD ["python", "vivarium_biosimulators/experiments/test_biosimulators.py", "-e", "0"]
