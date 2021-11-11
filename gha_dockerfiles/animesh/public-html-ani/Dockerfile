# Base image https://hub.docker.com/u/rocker/
FROM rocker/shiny-verse:4.0.3

LABEL author="Tim M.Schendzielorz docker@timschendzielorz.com" 

# system libraries of general use
# install debian packages
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
    libxml2-dev \
    libcairo2-dev \
    libpq-dev \
    libssh2-1-dev \
    libcurl4-openssl-dev \
    libssl-dev


## update system libraries
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean

# copy necessary files
## app folder
COPY /diffExpr ./app
## renv.lock file
COPY /renv.lock ./renv.lock

# install renv & restore packages
RUN Rscript -e 'install.packages("webshot")'
#RUN Rscript -e 'renv::restore()'

# remove install files
RUN rm -rf /var/lib/apt/lists/*

# make all app files readable, gives rwe permisssion (solves issue when dev in Windows, but building in Ubuntu)
RUN chmod -R 755 /app

# expose port (for local deployment only)
EXPOSE 3838 

# set non-root
RUN useradd shiny_user
USER shiny_user

# run app on container start (use heroku port variable for deployment)
CMD ["R", "-e", "shiny::runApp('/app', host = '0.0.0.0', port = as.numeric(Sys.getenv('PORT')))"]