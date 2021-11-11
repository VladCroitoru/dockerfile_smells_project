FROM rocker/rstudio-stable:latest

LABEL   org.label-schema.name = "Docker for Statistical Rethinking with RStudio" \
        org.label-schema.license = "MIT" \
        org.label-schema.vcs-url = "https://github.com/thacoon/docker-rethinking"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        zlib1g-dev \
    && cd /usr/local/lib/R/etc \
    && sed -i '/CPPFLAGS = -I\/usr\/local\/include/c CPPFLAGS = -I\/usr\/local\/include -DBOOST_PHOENIX_NO_VARIADIC_EXPRESSION' Makeconf \
    && sed -i '/CXXFLAGS = -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g $(LTO)/c CXXFLAGS = -g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g $(LTO) -DBOOST_PHOENIX_NO_VARIADIC_EXPRESSION' Makeconf \
    && cd / \
    && Rscript -e "install.packages('rstan', repos='https://cloud.r-project.org/', dependencies=TRUE)" \
    && Rscript -e "install.packages(c('coda', 'mvtnorm', 'devtools'))" \
    && Rscript -e "library('devtools'); devtools::install_github('rmcelreath/rethinking')" \
    && chmod 777 /tmp \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/ \
    && rm -rf /tmp/*
