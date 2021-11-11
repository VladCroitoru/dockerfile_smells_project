FROM rocker/shiny

RUN apt-get update && \
    apt-get install -y git libxml2-dev libssl-dev ghostscript
 
# Install DNAlandscapeR
COPY . /srv/shiny-server/DNAlandscapeR
 
WORKDIR /srv/shiny-server/DNAlandscapeR

# Install packrat packages
RUN Rscript -e 'install.packages("packrat"); \
                packrat::restore()'
# Make special installs
RUN githubsha1=`cat packrat/packrat.lock | grep -A4 diffloop | grep GithubSha1 | cut -f2 -d":" | tr -d ' '`; R CMD INSTALL packrat/src/diffloop/$githubsha1.tar.gz
RUN Rscript -e 'devtools::install_github("s-u/PKI"); \
                devtools::install_github("rstudio/rsconnect")'

# Temporary permissions hack
RUN chown shiny:shiny -R packrat && \
    chown shiny:shiny .gitignore 

# Serve only the DNAlandscapeR app (replace /srv/shiny-server with /srv/shiny-server/DNAlandscapeR)
RUN sed -i 's/\/srv\/shiny-server/\/srv\/shiny-server\/DNAlandscapeR/' /etc/shiny-server/shiny-server.conf

# Improve first page load time by not shutting down the R session when idle
RUN sed -i '/location \/ {/a app_idle_timeout 14400;' /etc/shiny-server/shiny-server.conf

# Increase app load timeout
RUN sed -i '/location \/ {/a app_init_timeout 60;' /etc/shiny-server/shiny-server.conf

# Add Google Analytics tracking code
RUN sed -i '/location \/ {/a google_analytics_id UA-37764824-4;' /etc/shiny-server/shiny-server.conf

# Start and expose shiny server
EXPOSE 3838
CMD /usr/bin/shiny-server.sh

