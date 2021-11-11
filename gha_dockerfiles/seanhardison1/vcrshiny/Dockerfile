FROM rocker/r-ver:4.0.5
RUN apt-get update && apt-get install -y  git-core libcurl4-openssl-dev libgit2-dev libicu-dev libpng-dev libssl-dev libxml2-dev make pandoc pandoc-citeproc && rm -rf /var/lib/apt/lists/*
RUN echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl', Ncpus = 4)" >> /usr/local/lib/R/etc/Rprofile.site
RUN R -e 'install.packages("remotes")'
RUN Rscript -e 'remotes::install_version("magrittr",upgrade="never", version = "2.0.1")'
RUN Rscript -e 'remotes::install_version("glue",upgrade="never", version = "1.4.2")'
RUN Rscript -e 'remotes::install_version("processx",upgrade="never", version = "3.5.1")'
RUN Rscript -e 'remotes::install_version("htmltools",upgrade="never", version = "0.5.1.1")'
RUN Rscript -e 'remotes::install_version("stringr",upgrade="never", version = "1.4.0")'
RUN Rscript -e 'remotes::install_version("ggplot2",upgrade="never", version = "3.3.3")'
RUN Rscript -e 'remotes::install_version("zoo",upgrade="never", version = "1.8-9")'
RUN Rscript -e 'remotes::install_version("pkgload",upgrade="never", version = "1.2.1")'
RUN Rscript -e 'remotes::install_version("attempt",upgrade="never", version = "0.3.1")'
RUN Rscript -e 'remotes::install_version("shiny",upgrade="never", version = "1.6.0")'
RUN Rscript -e 'remotes::install_version("lubridate",upgrade="never", version = "1.7.10")'
RUN Rscript -e 'remotes::install_version("dplyr",upgrade="never", version = "1.0.6")'
RUN Rscript -e 'remotes::install_version("xts",upgrade="never", version = "0.12.1")'
RUN Rscript -e 'remotes::install_version("usethis",upgrade="never", version = "2.0.1")'
RUN Rscript -e 'remotes::install_version("testthat",upgrade="never", version = "3.0.2")'
RUN Rscript -e 'remotes::install_version("config",upgrade="never", version = "0.3.1")'
RUN Rscript -e 'remotes::install_version("shinyWidgets",upgrade="never", version = "0.6.0")'
RUN Rscript -e 'remotes::install_version("shinyjs",upgrade="never", version = "2.0.0")'
RUN Rscript -e 'remotes::install_version("ggtext",upgrade="never", version = "0.1.1")'
RUN Rscript -e 'remotes::install_version("tsibble",upgrade="never", version = "1.0.1")'
RUN Rscript -e 'remotes::install_version("tidyr",upgrade="never", version = "1.1.3")'
RUN Rscript -e 'remotes::install_version("readr",upgrade="never", version = "1.4.0")'
RUN Rscript -e 'remotes::install_version("leaflet",upgrade="never", version = "2.0.4.1")'
RUN Rscript -e 'remotes::install_version("shinyFeedback",upgrade="never", version = "0.3.0")'
RUN Rscript -e 'remotes::install_version("ggsci",upgrade="never", version = "2.9")'
RUN Rscript -e 'remotes::install_version("dygraphs",upgrade="never", version = "1.1.1.6")'
RUN Rscript -e 'remotes::install_version("shinythemes",upgrade="never", version = "1.2.0")'
RUN Rscript -e 'remotes::install_version("DT",upgrade="never", version = "0.18")'
RUN Rscript -e 'remotes::install_version("golem",upgrade="never", version = "0.3.1")'
RUN mkdir /build_zone
ADD . /build_zone
WORKDIR /build_zone
RUN R -e 'remotes::install_local(upgrade="never")'
RUN rm -rf /build_zone
EXPOSE 80
CMD R -e "options('shiny.port'=80,shiny.host='0.0.0.0');vcrshiny::run_app()"
