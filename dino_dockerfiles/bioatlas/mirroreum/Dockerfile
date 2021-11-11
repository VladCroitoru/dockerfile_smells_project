FROM rocker/ropensci:3.4.1

RUN rm -vfr /var/lib/apt/lists/*

COPY ./sources.list /etc/apt/sources.list
COPY ./installGithub.r /usr/local/lib/R/site-library/littler/examples/installGithub.r
COPY ./installGithub.r /usr/local/bin/installGithub.r

RUN apt-get update && apt-get install -y \
	proj-bin \
	gdal-bin \
	libhdf4-dev \
	netcdf-bin \
	libnlopt-dev \
&& install2.r --error \
	sparklyr \
	downscale \
	getopt \
	xfun \
	tufte \
	tufterhandout \
	ggmap \
	rticles \
	tint \
	cartogram \
	randomForest \
	Rserve \
	caret \
	treemap \
	AICcmodavg \
	SDMTools \
	ade4 \
	adehabitatHR \
	adehabitatMA \
	maptools \
	shapefiles \
	alphahull \
	crayon \
	SSDM \
	BIEN \
	spatstat \
	Grid2Polygons \
	googleVis \
	spacetime \
	plotKML \
	pdfCluster \
	move \
	maxnet \
	red

# add packages for zoa

RUN wget -P /tmp 'https://github.com/positioning/kalmanfilter/raw/master/downloads/R3x/64bit/linux/kftrack_0.70-x64.tar.gz' && \
	wget -P /tmp 'https://github.com/positioning/kalmanfilter/raw/master/downloads/R3x/64bit/linux/ukfsst_0.3-x64.tar.gz' && \
	Rscript -e "install.packages('/tmp/kftrack_0.70-x64.tar.gz', repos=NULL)" && \
	Rscript -e "install.packages(c('date', 'ncdf'), repos='http://cran.csiro.au/')" && \
	Rscript -e "install.packages('/tmp/ukfsst_0.3-x64.tar.gz', repos=NULL)"

# add GitHub and Ecology packages
RUN installGithub.r --deps TRUE \
	AtlasOfLivingAustralia/ALA4R \
	azizka/sampbias \
	azizka/speciesgeocodeR \
	raquamaps/raquamaps \
	mskyttner/swedishbirdtrends \
	mskyttner/swedishbirdrecoveries \
	fschirr/VirSysMon

RUN apt-get update && apt-get install -y \
    gdebi-core \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev && \
    wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb && \
    R -e "install.packages(c('shiny', 'rmarkdown'), repos='https://cran.rstudio.com/')" && \
    cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 3838

COPY shiny-server.sh /usr/bin/shiny-server.sh

# clean out example and deploy swedishbirdrecoveries in root context

RUN rm /srv/shiny-server/index.html && \
	rm -rf /srv/shiny-server/sample-apps && \
	ln -s /usr/local/lib/R/site-library/swedishbirdrecoveries/shiny-apps/birdrecoveries/* /srv/shiny-server

# add more packages
RUN install2.r --error \
	reprex \
	pool \
	RPostgres \
	rasterVis \
	cowplot

RUN installGithub.r --deps FALSE \
	GBIF-Europe/darwinator \
	raymondben/livingatlases \
	rekonstrukt/swedishbutterflies

# install.packages(c("downscale", "split", "top", ), 
#  repos="http://R-Forge.R-project.org", dependencies = TRUE)

RUN apt-get update && apt-get install -y \
	tesseract-ocr-swe

RUN rm -rf /tmp/*.rds && \
	apt-get autoclean && \
	apt-get autoremove -y

RUN pip install suds-jurko lxml && \
	install2.r --error \
	tabulizer \
	magick \
	tesseract

# CMD ["/usr/bin/shiny-server.sh"]
