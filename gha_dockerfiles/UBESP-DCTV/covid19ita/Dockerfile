FROM rocker/r-ver:4.0.3

ARG GITHUB_PAT

RUN apt-get update && apt-get install -y  git-core libcurl4-openssl-dev libgit2-dev libicu-dev libpng-dev libsodium-dev libssl-dev libxml2-dev make pandoc pandoc-citeproc zlib1g-dev libmariadbclient-dev && rm -rf /var/lib/apt/lists/*
RUN echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/local/lib/R/etc/Rprofile.site

RUN echo "'GITHUB_PAT=$GITHUB_PAT'" >> /usr/local/lib/R/etc/Renviron.site

RUN R -e 'install.packages("remotes")'
RUN R -e 'remotes::install_github("r-lib/remotes", ref = "97bbf81")'
RUN Rscript -e 'remotes::install_version("magrittr",upgrade="never", version = "2.0.1")'
RUN Rscript -e 'remotes::install_version("lifecycle",upgrade="never", version = "0.2.0")'
RUN Rscript -e 'remotes::install_version("glue",upgrade="never", version = "1.4.2")'
RUN Rscript -e 'remotes::install_version("cli",upgrade="never", version = "2.2.0")'
RUN Rscript -e 'remotes::install_version("processx",upgrade="never", version = "3.4.4")'
RUN Rscript -e 'remotes::install_version("withr",upgrade="never", version = "2.3.0")'
RUN Rscript -e 'remotes::install_version("stringr",upgrade="never", version = "1.4.0")'
RUN Rscript -e 'remotes::install_version("pkgload",upgrade="never", version = "1.1.0")'
RUN Rscript -e 'remotes::install_version("RColorBrewer",upgrade="never", version = "1.1-2")'
RUN Rscript -e 'remotes::install_version("xts",upgrade="never", version = "0.12.1")'
RUN Rscript -e 'remotes::install_version("testthat",upgrade="never", version = "3.0.0")'
RUN Rscript -e 'remotes::install_version("scales",upgrade="never", version = "1.1.1")'
RUN Rscript -e 'remotes::install_version("httr",upgrade="never", version = "1.4.2")'
RUN Rscript -e 'remotes::install_version("ggplot2",upgrade="never", version = "3.3.2")'
RUN Rscript -e 'remotes::install_version("zoo",upgrade="never", version = "1.8-8")'
RUN Rscript -e 'remotes::install_version("forecast",upgrade="never", version = "8.13")'
RUN Rscript -e 'remotes::install_version("purrr",upgrade="never", version = "0.3.4")'
RUN Rscript -e 'remotes::install_version("fs",upgrade="never", version = "1.5.0")'
RUN Rscript -e 'remotes::install_version("htmltools",upgrade="never", version = "0.5.0")'
RUN Rscript -e 'remotes::install_version("attempt",upgrade="never", version = "0.3.1")'
RUN Rscript -e 'remotes::install_version("greybox",upgrade="never", version = "0.6.4")'
RUN Rscript -e 'remotes::install_version("shiny",upgrade="never", version = "1.5.0")'
RUN Rscript -e 'remotes::install_version("tidyr",upgrade="never", version = "1.1.2")'
RUN Rscript -e 'remotes::install_version("htmlwidgets",upgrade="never", version = "1.5.2")'
RUN Rscript -e 'remotes::install_version("usethis",upgrade="never", version = "1.6.3")'
RUN Rscript -e 'remotes::install_version("roxygen2",upgrade="never", version = "7.1.1")'
RUN Rscript -e 'remotes::install_version("here",upgrade="never", version = "1.0.0")'
RUN Rscript -e 'remotes::install_version("config",upgrade="never", version = "0.3")'
RUN Rscript -e 'remotes::install_version("spelling",upgrade="never", version = "2.2")'
RUN Rscript -e 'remotes::install_version("readr",upgrade="never", version = "1.4.0")'
RUN Rscript -e 'remotes::install_version("lintr",upgrade="never", version = "2.0.1")'
RUN Rscript -e 'remotes::install_version("covr",upgrade="never", version = "3.5.1")'
RUN Rscript -e 'remotes::install_version("assertive",upgrade="never", version = "0.3-6")'
RUN Rscript -e 'remotes::install_version("smooth",upgrade="never", version = "3.0.0")'
RUN Rscript -e 'remotes::install_version("tscount",upgrade="never", version = "1.4.3")'
RUN Rscript -e 'remotes::install_version("sodium",upgrade="never", version = "1.1")'
RUN Rscript -e 'remotes::install_version("slider",upgrade="never", version = "0.1.5")'
RUN Rscript -e 'remotes::install_version("shinyWidgets",upgrade="never", version = "0.5.4")'
RUN Rscript -e 'remotes::install_version("shinyjs",upgrade="never", version = "2.0.0")'
RUN Rscript -e 'remotes::install_version("shinydashboard",upgrade="never", version = "0.7.1")'
RUN Rscript -e 'remotes::install_version("RJSONIO",upgrade="never", version = "1.3-1.4")'
RUN Rscript -e 'remotes::install_version("RCurl",upgrade="never", version = "1.98-1.2")'
RUN Rscript -e 'remotes::install_version("plotly",upgrade="never", version = "4.9.2.1")'
RUN Rscript -e 'remotes::install_version("lubridate",upgrade="never", version = "1.7.9.2")'
RUN Rscript -e 'remotes::install_version("leaflet",upgrade="never", version = "2.0.3")'
RUN Rscript -e 'remotes::install_version("golem",upgrade="never", version = "0.2.1")'
RUN Rscript -e 'remotes::install_version("gam",upgrade="never", version = "1.20")'
RUN Rscript -e 'remotes::install_version("DT",upgrade="never", version = "0.16")'
RUN Rscript -e 'remotes::install_github("tidyverse/tibble@9eeef4df1a0d74469d9e04df44d909bbeba9544d")'
RUN Rscript -e 'remotes::install_github("tidyverse/dplyr@872dbd810c0815cc69b3be991b6a64ed21a72484")'
RUN Rscript -e 'remotes::install_github("UBESP-DCTV/covid19.icuve@b30e71a84d4e1329620f0d9646e3ba62fee199a0")'
RUN Rscript -e 'remotes::install_github("sprouffske/growthcurver@ae969abe0e3d0a6b67052a5fa085f9a638d5e9a1")'

RUN mkdir /build_zone
ADD . /build_zone
WORKDIR /build_zone
RUN R -e 'remotes::install_local(upgrade="never")'

EXPOSE 3838

CMD  ["R", "-e", "options('shiny.port'=3838,shiny.host='0.0.0.0');covid19ita::run_app()"]
