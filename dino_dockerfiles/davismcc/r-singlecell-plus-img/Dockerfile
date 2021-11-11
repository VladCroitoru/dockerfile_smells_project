FROM davismcc/r-singlecell-img
LABEL authors="davismcc@gmail.com" \
    maintainer="Davis McCarthy <davismcc@gmail.com>" \
    description="Docker image containing latest R with packages for single-cell analyses"
 
RUN mkdir -p /usr/local/lib/R/site-library
ADD install.R /tmp/
RUN R -f /tmp/install.R
