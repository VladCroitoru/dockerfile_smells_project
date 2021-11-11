FROM rocker/tidyverse:3.3.1

MAINTAINER "Ellis Valentiner" ellis.valentiner@gmail.com
LABEL version="0.5"

RUN sudo apt-get update && \
	apt-get -y install \
		gdal-bin \
		libgdal-dev \
		libproj-dev

RUN Rscript -e 'install.packages(c("shiny", "raster", "rgdal"))'

ADD ./ /home/rstudio/
WORKDIR /home/rstudio/

EXPOSE 3838

CMD ["R","-e","shiny::runApp('.', host='0.0.0.0', port=3838)"]