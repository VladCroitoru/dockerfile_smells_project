FROM martinsoto/pyrocksdb:latest

MAINTAINER Martin Soto <donsoto@gmail.com>

RUN pip install jupyter

# Install Tini (as done in
# https://github.com/jupyter/docker-stacks/blob/master/minimal-notebook/Dockerfile). Jupyter
# won't run correctly without an init process.
RUN curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini > /bin/tini && \
    echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b /bin/tini" | sha256sum -c - && \
    chmod +x /bin/tini
ENTRYPOINT ["tini", "--"]

# Add a regular user to run Jupyter.
RUN useradd -m -s /bin/bash -N -u 1000 jupyter

# Work directory.
RUN mkdir /notebooks && chown jupyter: /notebooks

CMD jupyter notebook --no-browser --ip=0.0.0.0 --port=8888
EXPOSE 8888

WORKDIR /notebooks
USER jupyter
