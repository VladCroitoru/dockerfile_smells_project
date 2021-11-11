#     ____                _____ _    __
#    / __ \ ____   ____  / ___/| |  / /
#   / /_/ // __ \ / __ \ \__ \ | | / / 
#  / ____// /_/ // /_/ /___/ / | |/ /  
# /_/     \____// .___//____/  |___/   
#              /_/                     
#
# Banner at http://patorjk.com/software/taag/#p=display&h=1&v=2&f=Slant&t=PopSV


## Pull base image
FROM bioconductor/release_base

## Install required packages
RUN install2.r --error \
    -r "https://cran.rstudio.com" \
    -r "http://www.bioconductor.org/packages/release/bioc" \
    devtools \
    Rsamtools \
    DNAcopy \
  && installGithub.r jmonlong/PopSV \
  && rm -rf /tmp/downloaded_packages/ /tmp/*.rds

## Set working directory
WORKDIR /root

## Copy useful genome binning (in order to avoid installing heavy BSgenome.Hsapiens.UCSC.hg19)
COPY bins-500bp.RData ./
COPY bins-1kbp.RData ./
COPY bins-2kbp.RData ./
COPY bins-5kbp.RData ./

## Clone GitHub Repo
RUN git clone https://github.com/jmonlong/PopSV.git
