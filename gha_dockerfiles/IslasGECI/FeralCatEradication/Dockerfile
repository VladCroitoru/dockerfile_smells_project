FROM islasgeci/base:0.7.0
COPY . /workdir
RUN Rscript -e "install.packages(c('comprehenr', 'latex2exp', 'plotly'), repos='http://cran.rstudio.com')"
RUN Rscript -e "install.packages(c('covr', 'devtools', 'lintr', 'roxygen2', 'styler', 'testthat', 'vdiffr'), repos='http://cran.rstudio.com')"

RUN R CMD build . && \
	R CMD INSTALL FeralCatEradication_0.2.2.tar.gz
