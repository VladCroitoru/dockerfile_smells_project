FROM fjukstad/kvik-r

RUN apt-get update  && \
    apt-get install -y default-jre \
    default-jdk \
    libmariadb-client-lgpl-dev
    

# Install R package dependencies 
RUN R -e 'install.packages(c("ggplot2", "Hmisc", "Rcpp", "roxygen2", "jsonlite", "igraph", "dplyr", "parallel", "colorspace", "ic10", "igraph", "network","GGally","sna", "animation", "devtools"), repos="http://cran.rstudio.com")'
RUN R -e 'source("https://bioconductor.org/biocLite.R"); biocLite(c("genefu", "WGCNA", "impute", "preprocessCore", "GO.db", "illuminaHumanv4.db", "illuminaHumanv3.db","hgu133a.db"), dependencies=TRUE)'

RUN R -e 'devtools::install_github("vdumeaux/mixtR")'
RUN R -e 'devtools::install_github("vdumeaux/mixtApp")'

WORKDIR /go/src/github.com/fjukstad/kvik/r/examples
