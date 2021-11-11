FROM rocker/ropensci
MAINTAINER Hector Corrada Bravo <hcorrada@gmail.com>

# install datasets from ISL
RUN install2.r --error \
    ISLR \
    gapminder \
    cvTools \
    tree \
    e1071 \
    ROCR \
    randomForest

# install hadley's excel reader package
RUN installGithub.r \
    hadley/readxl

# financial data package
RUN install2.r --error \
    quantmod \
    swirl


 # make a directory for tidy and wrangling unit
RUN mkdir -p /home/ids_materials/tidy_unit && chown -R rstudio /home/ids_materials

# download the datasets for the tidy unit
RUN cd /home/ids_materials/tidy_unit && \
  git clone https://github.com/hadley/tidyr.git && \
  mv tidyr/vignettes example_data && \
  rm -rf tidyr


# Lahman's baseball dataset

# install sqlite cli
RUN apt-get update \
      && apt-get install -y --no-install-recommends \
        sqlite3 \
        libsqlite3-dev

# create directory for data
# download readme file to directory
# download sqlite dataset from github
# copy sqlite file to data directory
RUN mkdir -p /home/ids_materials/lahman_sqlite \
  && wget -O /home/ids_materials/lahman_sqlite/readme2014.txt http://seanlahman.com/files/database/readme2014.txt \
  && git clone https://github.com/jknecht/baseball-archive-sqlite.git /tmp/lahman_sqlite \
  && cp /tmp/lahman_sqlite/lahman2014.sqlite /home/ids_materials/lahman_sqlite

RUN chmod a+w -R /home/ids_materials/lahman_sqlite

# copy genotype data into data directory
COPY example_data/geno_data.rda /home/ids_materials/

