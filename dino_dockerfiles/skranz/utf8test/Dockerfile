FROM rocker/tidyverse

COPY add_shiny.sh /etc/cont-init.d/add
RUN export ADD=shiny && bash /etc/cont-init.d/add

# The copy command below seems not to work.
# So I link the app directory in docker run

# COPY app.R /srv/shiny-server/utf8test/
