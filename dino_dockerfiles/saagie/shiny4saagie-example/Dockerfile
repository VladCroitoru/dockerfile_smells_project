FROM saagie/shiny4saagie

# Install R packages required by your Shiny app
RUN R -e 'install.packages(c("DT", "magrittr"), repos="http://cloud.r-project.org")'

# Copy your Shiny app to /srv/shiny-server/myapp
COPY myapp /srv/shiny-server/myapp

# Launch Shiny Server
CMD ["/usr/bin/shiny-server.sh"]
