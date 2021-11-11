FROM jupyter/minimal-notebook:db3ee82ad08a

MAINTAINER Saagie

USER root

# Julia Installation
RUN apt-get update && apt-get install --no-install-recommends -y \
    libtool software-properties-common python-software-properties \
    libx11-dev libpng3 gettext tcl8.5 libpango1.0-0 tk8.5 hdf5-tools && \
    apt-get clean


# Install Julia v0.6.2
RUN cd /tmp && \
    wget https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.2-linux-x86_64.tar.gz && \
    tar xzf julia-0.6.2-linux-x86_64.tar.gz && rm julia-0.6.2-linux-x86_64.tar.gz && \
    mv julia-* /opt/julia_0.6.2 && chmod -R 777 /opt/julia_0.6.2 && \
    ln -s /opt/julia_0.6.2/bin/julia /usr/local/bin/julia

USER $NB_USER

# Have root install julia packages globally.
# Find this directory by looking at `LOAD_PATH` from within a julia session.
ENV JULIA_PKGDIR /opt/julia_0.6.2/share/julia/site/

# Julia package Installation (should be global)
RUN julia -e 'Pkg.init(); Pkg.add("IJulia")' && \
   julia -e 'Pkg.add("Gadfly"); Pkg.add("RDatasets"); Pkg.add("ForwardDiff")' && \
   julia -e 'Pkg.add("Distributions"); Pkg.add("NLsolve"); Pkg.add("Interact")' && \
   julia -e 'Pkg.add("PyCall"); Pkg.add("PyPlot"); Pkg.add("Pandas"); Pkg.add("Winston")' && \
   julia -e 'Pkg.add("QuantEcon"); Pkg.add("Mongo"); Pkg.add("Hive");'

# check out ZMQ and IJulia to get them working
RUN julia -e 'Pkg.checkout("ZMQ"); Pkg.checkout("IJulia");'

# Create default workdir (useful if no volume mounted)
USER root
RUN mkdir /notebooks-dir && chown 1000:100 /notebooks-dir
USER $NB_USER

# Define default workdir
WORKDIR /notebooks-dir

# Default: run without authentication
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
