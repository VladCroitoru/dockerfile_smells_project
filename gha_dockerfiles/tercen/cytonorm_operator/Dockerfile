FROM tercen/runtime-r40:4.0.4-1

ENV RENV_VERSION 0.14.0
RUN R -e "install.packages('remotes', repos = c(CRAN = 'https://cran.r-project.org'))"
RUN R -e "remotes::install_github('rstudio/renv@${RENV_VERSION}')"

COPY . /operator
WORKDIR /operator

RUN apt-get update
RUN apt-get install -y r-cran-tcltk2

RUN git clone https://github.com/tercen/cytonorm_operator.git

WORKDIR /operator/cytonorm_operator

RUN echo 1.1.4 && git pull
RUN git checkout 1.1.4

RUN R -e "renv::consent(provided=TRUE);renv::restore(confirm=FALSE)"

ENV TERCEN_SERVICE_URI https://tercen.com

ENTRYPOINT [ "R","--no-save","--no-restore","--no-environ","--slave","-f","main.R", "--args"]
CMD [ "--taskId", "someid", "--serviceUri", "https://tercen.com", "--token", "sometoken"]
