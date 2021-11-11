FROM r-base

RUN apt-get update
RUN apt-get install curl libcurl4-openssl-dev libssl-dev g++ -y
RUN R -e "install.packages('https://cran.r-project.org/src/contrib/Archive/curl/curl_0.9.7.tar.gz')"
RUN R -e "install.packages('bigrquery')"
RUN R -e "install.packages('https://cran.r-project.org/src/contrib/Archive/BH/BH_1.62.0-1.tar.gz')"
RUN R -e "install.packages('rstan')"
RUN R -e "install.packages('prophet')"
RUN R -e "install.packages('data.table')"
RUN R -e "install.packages('dplyr')"
RUN R -e "install.packages('sqldf')"
RUN R -e "ifelse('bigrquery' %in% rownames(installed.packages()), quit('yes', 0), quit('yes', 1))"
RUN R -e "ifelse('prophet' %in% rownames(installed.packages()), quit('yes', 0), quit('yes', 1))"
RUN R -e "ifelse('dplyr' %in% rownames(installed.packages()), quit('yes', 0), quit('yes', 1))"
RUN R -e "ifelse('sqldf' %in% rownames(installed.packages()), quit('yes', 0), quit('yes', 1))"

COPY . /src
WORKDIR /src
