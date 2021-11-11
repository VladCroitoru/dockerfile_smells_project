from r-base

# system libraries of general use
RUN apt-get update  -qq \
 && apt-get upgrade -y

RUN apt-get install -y --no-install-recommends --allow-downgrades \
	apt-utils \
	default-jdk \
	libssl-dev \
	libxml2-dev \
	libcurl3-dev \
	libcurl4-openssl-dev \
	&& rm -rf /var/lib/apt/lists/*

RUN apt-get update -qq

RUN R -e "install.packages('shiny' ,dep=T)" 
RUN R -e "install.packages('shinydashboard' ,dep=T)" 
RUN R -e "install.packages('stringr' ,dep=T)" 
RUN R -e "install.packages('shinyjs', dep=T)"
RUN R -e "install.packages('ggthemes' ,dep=T)" 
RUN R -e "install.packages('lubridate' ,dep=T)" 
RUN R -e "install.packages('shinyBS' ),dep=T)"
RUN R -e "install.packages('ggplot2' ,dep=T)" 
RUN R -e "install.packages('plotly' ,dep=T)" 
RUN R -e "install.packages('AppliedPredictiveModeling' ,dep=T)" 
RUN R -e "install.packages('caret' ,dep=T)" 
RUN R -e "install.packages('scales' ,dep=T)" 
RUN R -e "install.packages('mice' ,dep=T)" 
RUN R -e "install.packages('randomForest' ,dep=T)" 
RUN R -e "install.packages('reshape' ,dep=T)" 
RUN R -e "install.packages('rpart'  ),dep=T)" 
RUN R -e "install.packages('DT' ,dep=T)" 
RUN R -e "install.packages('xtable' ,dep=T)" 
RUN R -e "install.packages('dplyr' ,dep=T)" 
RUN R -e "install.packages('XLConnect' ,dep=T)" 
RUN R -e "install.packages('tidyverse' ,dep=T)" 

#RUN R -e "install.packages('htmlwidgets'  ),dep=T)" 


