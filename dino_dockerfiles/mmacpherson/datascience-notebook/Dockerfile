FROM jupyter/datascience-notebook

# -- from the docs:
#    tensorflow-notebook inherits from scipy-notebook, which provides:
#
#    beautifulsoup
#    bokeh
#    cloudpickle
#    cython
#    dill
#    jupyter
#    matplotlib
#    numba
#    numpy
#    pandas
#    patsy
#    scikit-image
#    scikit-learn
#    scipy
#    seaborn
#    statsmodels
#    sympy
#    vincent
#
#    (https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook)
#
#
#    then the tensorflow notebook adds
#
#    keras
#    tensorflow
#
#    (https://github.com/jupyter/docker-stacks/tree/master/tensorflow-notebook)

LABEL maintainer="Mike Macpherson <mmacpherson@users.noreply.github.com>"

USER root
RUN apt-get update && apt-get install -y \
    awscli \
    default-jre \
    ed \
    git-core \
    libhdf5-dev \
    libnlopt-dev \
    libomp-dev \
  && rm -rf /var/lib/apt/lists/*

ARG JDK_CERTS_URL=https://circle-downloads.s3.amazonaws.com/circleci-images/cache/linux-amd64/openjdk-9-slim-cacerts
ARG LEIN_URL=https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
RUN curl -s -o /etc/ssl/certs/java/cacerts $JDK_CERTS_URL \
    && curl -s -o /usr/local/bin/lein $LEIN_URL \
    && chmod +x /usr/local/bin/lein \
    && lein version # called for side effect of installation on first run

USER $NB_USER
# -- upgrade everything
#    (relies on earlier-configured conda channels: first conda-forge, then defaults)
RUN conda update --all --quiet --yes

# -- add packages available in conda
#    (relies on earlier-configured conda channels: first conda-forge, then defaults)
RUN conda install --quiet --yes \
    # -- general
    boto3 \
    dask \
    ipython \
    luigi \
    click \
    # -- web/net
    bottle \
    flask \
    # pelican \
    requests \
    # -- viz
    # altair \
    plotnine \
    # -- data
    # feather-format \
    protobuf \
    pymc3 \
    # pystan \
    # pytorch \
    # theano \
    xgboost \
    # -- coding
    flake8 \
    hypothesis \
    jupyter_contrib_nbextensions \
    jupyterlab \
    mypy \
    nbstripout \
    pytest \
    watermark \
    yapf \
    # -- R
    r-arm \
    r-caret \
    r-domc \
    r-effects \
    r-feather \
    r-glmnet \
    r-irkernel \
    r-proc \
    r-rocr \
    r-speedglm \
    r-tidyverse \
    && conda clean -tipsy

# -- install python packages not available in the conda channels above
RUN pip install -U -q pip && \
    pip install -U -q \
        dash \
        dash-core-components \
        dash-html-components \
        dash-renderer \
        edward \
        feather-format \
        knotr \
        plotly \
        plydata \
        pysistence \
        git+git://github.com/mmacpherson/cottonmouth.git@master

# -- install R packages not available in the conda channels above
# -- disabled "interplot" for now; dep "arm" unavailable
RUN R -e "install.packages(c('glmnetUtils', 'biglasso', 'interplot'), repos = 'http://cran.rstudio.com')"

# -- install clojure jupyter kernel
RUN conda install --quiet --yes \
  -c simplect \
  clojupyter \
  && conda clean -tipsy

WORKDIR $HOME
