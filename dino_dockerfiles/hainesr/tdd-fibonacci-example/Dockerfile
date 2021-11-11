#------------------------------------------------------------------------------
# TDD step-by-step example
#
# Adapted from Test-Driven Development By Example, Kent Beck.
#
# Robert Haines, University of Manchester, 2015
#
# BSD Licenced. See LICENCE for details.
#------------------------------------------------------------------------------

FROM jupyter/minimal-notebook:4.0
MAINTAINER Robert Haines <robert.haines@manchester.ac.uk>

COPY walkthrough-notebook.ipynb /home/jovyan/work/

# Convert notebooks to the current format and trust them
RUN find /home/jovyan/work -name '*.ipynb' -exec ipython nbconvert --to notebook {} --output {} \; && \
    chown -R jovyan:users /home/jovyan && \
    sudo -u jovyan env "PATH=$PATH" find /home/jovyan/work -name '*.ipynb' -exec ipython trust {} \;
