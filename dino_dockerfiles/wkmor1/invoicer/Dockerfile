FROM wkmor1/shiny-app
MAINTAINER William K Morris <wkmor1@gmail.com>

RUN    apt-get update \
    && apt-get install -y --no-install-recommends \
       lmodern \
       pandoc \
       tex-gyre \
       texlive \
       texlive-latex-extra

RUN    R -e "install.packages(c('rmarkdown', 'rhandsontable'))"

COPY   ui.R        /srv/shiny-server/
COPY   server.R    /srv/shiny-server/
COPY   invoice.Rmd /srv/shiny-server/
