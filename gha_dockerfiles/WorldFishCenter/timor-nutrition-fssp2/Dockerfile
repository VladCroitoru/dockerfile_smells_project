FROM rocker/geospatial:4.0.3

# Extra R packages
RUN install2.r drake here janitor skimr brms ggdist inspectdf
RUN install2.r config rnaturalearth rnaturalearthdata geodist ggrepel
RUN install2.r -r "http://packages.ropensci.org" rnaturalearthhires

# Rstudio interface preferences
COPY rstudio-prefs.json /home/rstudio/.config/rstudio/rstudio-prefs.json
