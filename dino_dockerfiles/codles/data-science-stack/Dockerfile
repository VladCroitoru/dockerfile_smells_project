FROM jupyter/datascience-notebook

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    xz-utils \
    vim \
    glances \
    lsb && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /bin/tar /bin/gtar 

USER $NB_USER

RUN conda create -y -n py27 python=2.7 anaconda
RUN /bin/bash -c "source activate py27 && \
    conda install -y jupyter && \
    python -m ipykernel install --user --name py27 --display-name "Python 2.7"    "
   
RUN jupyter labextension install @lckr/jupyterlab_variableinspector
   
RUN julia -e 'import Pkg; Pkg.update()' && \
    julia -e 'import Pkg; Pkg.add("HDF5")' && \
    julia -e 'import Pkg; Pkg.add("GR")' && \
    julia -e 'import Pkg; Pkg.add("Plots")' && \
    julia -e 'import Pkg; Pkg.add("Interact")' && \
    julia -e 'import Pkg; Pkg.add("RDatasets")' && \
    julia -e 'import Pkg; Pkg.add("DSP")' && \
    julia -e 'import Pkg; Pkg.add("BenchmarkTools")' && \
    # julia -e 'import Pkg; Pkg.add("PlotlyJS")' && \
    julia -e 'import Pkg; Pkg.add("SampledSignals")' && \
    julia -e 'import Pkg; Pkg.add("IJulia")' && \
    # Precompile Julia packages \
    julia -e 'import Pkg; using HDF5' && \
    julia -e 'import Pkg; using GR' && \
    julia -e 'import Pkg; using Plots' && \
    julia -e 'import Pkg; using Interact' && \
    julia -e 'import Pkg; using RDatasets' && \
    julia -e 'import Pkg; using DSP' && \
    julia -e 'import Pkg; using BenchmarkTools' && \
    julia -e 'import Pkg; using SampledSignals' && \
    # julia -e 'import Pkg; using PlotlyJS' && \
    julia -e 'import Pkg; using IJulia'
