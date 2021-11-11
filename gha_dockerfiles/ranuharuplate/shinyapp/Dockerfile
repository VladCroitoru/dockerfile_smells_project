FROM rocker/shiny

# Install system requirements for index.R as needed
# RUN apt-get update && apt-get install -y \
#     --no-install-recommends \
#     git-core \
#     libssl-dev \
#     libgdal-dev \
#     libcurl4-gnutls-dev \
#     curl \
#     libsodium-dev \
#     libxml2-dev \
#     libicu-dev \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# RUN R -e "install.packages(c('shinybusy','shinycssloaders','bs4Dash','fontawesome','ngram','xml','plotly','tidyverse','tmap','sf','raster','dplyr','DT','httr','RJSONIO','wordcloud','RColorBrewer','leaflet','rvest','htmltools','xml2','shinyBS','readxl','textclean'),  dependencies = TRUE, repos='http://cran.rstudio.com/')"
# RUN R -e "install.packages(c('bs4Dash'),  dependencies = TRUE, repos='http://cran.rstudio.com/')"
#  --error --skipinstalled
RUN install2.r shinydashboard
RUN install2.r bs4Dash
RUN install2.r shinyBS
RUN install2.r shinybusy
RUN install2.r shinycssloaders
RUN install2.r fontawesome
RUN install2.r httr
RUN install2.r RJSONIO
RUN install2.r dplyr
RUN install2.r DT
RUN install2.r devtools
RUN install2.r rvest
RUN install2.r wordcloud
RUN install2.r plotly
RUN install2.r readxl
RUN install2.r stringr
RUN install2.r ngram
RUN install2.r htmltools
RUN install2.r leaflet
RUN install2.r tidyverse
RUN install2.r textclean
RUN install2.r RColorBrewer
RUN install2.r raster
RUN install2.r tmap
RUN install2.r conflicted
RUN install2.r logging
RUN install2.r shinydashboardPlus
RUN install2.r log4r
RUN install2.r readr
RUN install2.r shinymanager
RUN install2.r shinyjs
RUN install2.r fresh
RUN install2.r shinyalert
RUN install2.r shinycssloaders
# RUN install2.r ggplot2

COPY ./app/ui.R /srv/shiny-server/
COPY ./app/server.R /srv/shiny-server/
COPY ./app/global.R /srv/shiny-server/

COPY ./app/src/pages/* /srv/shiny-server/src/pages/
COPY ./app/src/components/* /srv/shiny-server/src/components/
COPY ./app/www/* /srv/shiny-server/www/

COPY ./data/brand/Competitor_Database_-_Malaysia.xlsx /srv/shiny-server/data/brand/
COPY ./data/brand/ubersuggest/all_result_ubersuggest.csv /srv/shiny-server/data/brand/ubersuggest/

EXPOSE 3838

CMD ["/usr/bin/shiny-server"]

