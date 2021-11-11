FROM f0nzie/rstudio-keras
MAINTAINER Alfonso Reyes

# install tensorflow, keras inside R as rstudio user
# Python environment created under rstudio user
#USER rstudio

## install keras from within R
#RUN R -e "devtools::install_github('rstudio/keras')"
#RUN R -e "keras::install_keras()"

RUN install2.r --error \
    reshape


## install plot.nnet
# RUN R -e "devtools::source_url('https://gist.githubusercontent.com/fawda123/7471137/raw/466c1474d0a505ff044412703516c34f1a4684a5/nnet_plot_update.r')"

# add packages
RUN install2.r --error \
    boot \
    clusterGeneration \
    darch \
    FCNN4R \
    neuralnet \
    nnet \
    RcppDL \
    rnn \
    RSNNS


# USER root

