FROM python:2

LABEL name="apiary2postman docker image" \
      maintainer="rsvanda@gmail.com"

# Install apiary2postman tool
RUN pip install apiary2postman

# Install apiary2postman dependency - drafter
# HAS TO BE VERSION < v2
# see https://github.com/thecopy/apiary2postman#prerequisites
RUN git clone https://github.com/apiaryio/drafter && \
    cd drafter && \
    git checkout -b build v0.1.9 && \
    git submodule update --init --recursive && \
    ./configure && \
    make && \
    make install

# the binary should be executed on docker run
ENTRYPOINT ["apiary2postman"]