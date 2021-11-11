FROM skranz/shinyrstudio:latest
# A docker image for different tests

MAINTAINER Sebastian Kranz "sebastian.kranz@uni-ulm.de"

# copy and run package installation file
COPY install.r /tmp/install.r
RUN Rscript /tmp/install.r
