# Docker file for talkshow_guests
# Alexander Kleefeldt, Dec, 2017

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# install the ezknitr packages
RUN Rscript -e "install.packages('ezknitr', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"

# install gridExtra package
RUN Rscript -e "install.packages('gridExtra', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"

#install ggplot2 package
RUN Rscript -e "install.packages('ggplot2', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"

#install lubridate package
RUN Rscript -e "install.packages('lubridate', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"
