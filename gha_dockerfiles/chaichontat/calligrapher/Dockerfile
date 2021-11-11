FROM r-base:latest

RUN apt-get update
RUN apt-get -y install build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev \
    wget curl git ghostscript

RUN wget https://github.com/jgm/pandoc/releases/download/2.14.2/pandoc-2.14.2-1-amd64.deb && dpkg -i pandoc-2.14.2-1-amd64.deb

# ENV TINYTEX_VERSION=2021.08
RUN R -e "options(Ncpus = 2); \
    install.packages('devtools'); \
    devtools::install_github('rstudio/distill@33f858a0e56cd083d55d8ff8df2ed7eecd27372a');"

# # In order to use github CDN.
# RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh
# RUN R -e "tinytex::tlmgr('install changepage ifmtarg paralist placeins sauerj tufte-latex xifthen hardwrap titlesec ragged2e textcase setspace palatino fancyhdr units ulem morefloats fpl mathpazo pdfcrop biblatex logreq')"

# In order to use pdfcrop.
# ENV PATH="/root/.TinyTeX/bin/x86_64-linux:${PATH}"

RUN mkdir -p /github/workspace
WORKDIR /github/workspace

# Default theme
COPY theme/ /github/workspace/theme/

CMD r -e "rmarkdown::render(\"index.Rmd\", output_dir = \"./public\", output_format = \"all\")"
