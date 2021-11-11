FROM rocker/shiny:4.0.3

RUN apt-get update
RUN apt-get install --yes libxml2-dev
RUN apt-get install --yes libssl-dev
RUN apt-get install --yes libudunits2-dev
RUN apt-get install --yes libharfbuzz-dev libfribidi-dev
RUN apt-get install --yes libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev
RUN Rscript -e 'install.packages("shinyjs", repos="http://cran.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'install.packages("remotes", repos="http://cran.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'remotes::install_github("jpahle/CoRC")'
RUN Rscript -e 'install.packages("reshape2", repos="http://cran.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'install.packages("ggplot2", repos="http://cran.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'install.packages("shinyTree", repos="http://cran.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'install.packages("formattable", repos="http://cran.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'install.packages("XML", repos="http://cran.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'install.packages("DT", repos="http://cran.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'install.packages("tinytex", repos="http://cran.r-project.org", dependencies = TRUE)'
RUN Rscript -e 'tinytex::install_tinytex()'
COPY COPASI_web_mat3kk/ /srv/shiny-server/
WORKDIR /srv/shiny-server/overleaf_doc
RUN Rscript -e 'tinytex::pdflatex("main.tex", pdf_file="../www/dismolib.pdf")'
WORKDIR /srv/shiny-server
RUN sed -i "s/BUILD_TIMESTAMP/$(TZ=":America/New_York" date -Iseconds)/" ui.R
RUN chown -R shiny:shiny /srv/shiny-server
