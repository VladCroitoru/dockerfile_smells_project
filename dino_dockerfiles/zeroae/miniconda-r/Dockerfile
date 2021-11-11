FROM continuumio/miniconda

# This is here otherwise R does not install.
# We would like this step to be removed.
RUN set -ex \
    # STEP 0) We would like this to not be needed.
    && apt-get update -yqq \
    && apt-get install -y lsb-release binutils \
    && apt-get install -y libc-dev libcloog-isl4 libmpfr4 libmpc3 make \
    # clean up to minimize image layer size \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove $buildDeps

# Create the R Environment
RUN set -ex \
    # \
    # update conda \
    && conda update conda -y \
    # \
    # create R environment \
    && conda create -y -n r -c r gcc openjdk r-essentials r-rjava \
    && conda clean --tarballs --packages

# Set shell to BASH so we can source activate r and continue the rest of the work.
SHELL [ "/bin/bash", "-ce" ]

# This fails, libjvm.so was not linked to rJava using rpath
RUN source activate r \
    && R CMD javareconf \
    && R -e 'library(rJava)'
