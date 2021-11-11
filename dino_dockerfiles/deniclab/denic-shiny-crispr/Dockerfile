FROM centos:latest

RUN yum update -y && yum install -y epel-release && yum install -y R libcurl-devel openssl-devel wget

RUN mkdir -pv "/usr/share/doc/R-$(rpm -q --qf "%{VERSION}" R)/HTML"

RUN R -e "install.packages(c('assertthat', 'backports', 'base64enc', 'BH', 'bindr', 'bindrcpp', 'colorspace', 'dichromat', 'digest', 'dplyr', 'DT', 'evaluate', 'ggplot2', 'ggrepel', 'glue', 'gtable', 'highr', 'htmltools', 'htmlwidgets', 'httpuv', 'jsonlite', 'knitr', 'labeling', 'lazyeval', 'magrittr', 'markdown', 'mime', 'munsell', 'pkgconfig', 'plogr', 'plyr', 'R6', 'RColorBrewer', 'Rcpp', 'reshape2', 'rlang', 'rmarkdown', 'rprojroot', 'scales', 'shiny', 'sourcetools', 'stringi', 'stringr', 'tibble', 'viridisLite', 'xtable', 'yaml'), repos='https://cran.rstudio.com/', INSTALL_opts=c('--no-html', '--no-docs', '--without-keep.source', '--clean'))"

RUN mkdir /source
ADD . /source
WORKDIR /source

EXPOSE 80 8080 8443 443 3838

CMD ["/source/shiny-server.sh"]
