FROM rocker/ropensci
MAINTAINER Hector Corrada Bravo <hcorrada@gmail.com>


# install Spark
WORKDIR /home/root
RUN wget http://mirror.cogentco.com/pub/apache/spark/spark-1.4.0/spark-1.4.0.tgz
RUN tar zxvf spark-1.4.0.tgz
WORKDIR /home/root/spark-1.4.0
RUN build/mvn -DskipTests -Psparkr package

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

RUN install2.r --error \
    quantmod
    
    
    

