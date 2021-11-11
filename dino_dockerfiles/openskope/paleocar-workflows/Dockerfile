FROM  openskope/paleocar:0.1.0

ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN echo '****** Install Java 8 Runtime Environment'                                                \
 && apt-get -y install default-jre                                                                  \
                                                                                                    \
 && echo '***** Install graphviz for visualizing RestFlow workflows *****'                          \
 && apt-get -y install graphviz                                                                     \
                                                                                                    \
 && echo '***** install R packages for RestFlow R actor *****'                                      \
 && echo 'install.packages(c("optparse", "rjson"), repos="http://cran.us.r-project.org")'           \
    > /tmp/install_r_packages_for_restflow.R                                                        \
 && R --no-save < /tmp/install_r_packages_for_restflow.R                                            \
                                                                                                    \
 && echo '***** Download skope-restflow executable jar *****'                                       \
 && mkdir ~skope/bin                                                                                \
 && wget -O ~skope/bin/skope-restflow.jar https://github.com/openskope/skope-restflow/releases/download/v1.1.0/skope-restflow-1.1.0-jar-with-dependencies.jar

USER skope

ENTRYPOINT ["java", "-jar", "/home/skope/bin/skope-restflow.jar"]
