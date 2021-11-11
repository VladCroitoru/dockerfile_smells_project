FROM andrewheiss/tidyverse-stan:3.5.1
MAINTAINER Andrew Heiss andrewheiss@gmail.com

# Install project-specific packages
# Also, reinstall ggplot2 using a more recent snapshot, since ggplot2 3.0 
# was released after the R 3.5.1 MRAN snapshot was generated
RUN install2.r --error --deps TRUE \
        Amelia countrycode cshapes DT future furrr ggstance here \
        huxtable imputeTS lme4 OECD pander stargazer validate WDI \
    && R -e "library(devtools); \
        install.packages('ggplot2', repos = 'https://mran.revolutionanalytics.com/snapshot/2018-07-27/'); \
        install_github('bbolker/broom.mixed'); \
        install_github('thomasp85/patchwork');" \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds
