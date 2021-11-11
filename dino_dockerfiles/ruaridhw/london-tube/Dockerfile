FROM continuumio/miniconda3:latest
LABEL org.label-schema.license="GPL-2.0" \
      org.label-schema.vcs-url="https://github.com/ruaridhw/london-tube" \
      org.label-schema.vendor="" \
      maintainer="Ruaridh Williamson <ruaridh.williamson@gmail.com>"

# Install system dependencies
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >> /etc/apt/sources.list.d/pgdg.list \
  # Add postgres sources
  && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    # Required for mplleaflet
    libgl1-mesa-glx \
    # Required for RPostgreSQL
    libpq-dev postgresql-server-dev-9.6

# Conda provided binaries
RUN conda install -y -c conda-forge \
  # Install Python packages
  numpy pandas matplotlib lxml networkx requests \
  psycopg2 mplleaflet feather-format \
  click \
  # Install R and common packages
  r-base=3.4 r-tidyverse \
  r-feather r-data.table r-xml r-devtools r-dbi r-rprojroot \
  # CRAN packages built from conda-forge
  r-rgdal libgdal=2.1 r-rpostgresql \
  # JupyterLab and R Kernel
  jupyterlab r-irkernel

# Install GitHub- and pip-only packages
RUN Rscript -e "devtools::install_git('git://github.com/dantonnoriega/xmltools', dependencies = FALSE)" \
  && pip install smopy

EXPOSE 8888

ENV getwd /home/london-tube
RUN mkdir $getwd
WORKDIR $getwd

ENTRYPOINT ["tini", "--"]
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
