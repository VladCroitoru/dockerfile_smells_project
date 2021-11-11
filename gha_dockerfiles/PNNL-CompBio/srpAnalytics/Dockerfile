FROM rocker/tidyverse
# To setup other dependencies
RUN apt-get update -qq && apt-get install -y net-tools \
        python3.7 \
        python3-pip \
        curl \
        unixodbc

COPY setup.sh /setup.sh
RUN Rscript -e "install.packages('argparse')"

RUN /bin/bash ./setup.sh
COPY requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

COPY . srpAnalytics
WORKDIR srpAnalytics

ENTRYPOINT ["python3", "dataQcBmd.py"]
VOLUME ["/tmp"]
