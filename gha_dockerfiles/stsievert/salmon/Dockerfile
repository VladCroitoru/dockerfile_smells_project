FROM continuumio/miniconda3:4.10.3

RUN apt-get update
RUN apt-get install -y gcc cmake g++
RUN conda -V

COPY salmon.yml /salmon/salmon.yml
RUN conda env update -n base --file /salmon/salmon.yml --prune

VOLUME /salmon
VOLUME /data
COPY *.py *.cfg *.yml *.txt *.sh /salmon/
COPY ./salmon/ /salmon/salmon/
RUN ls /salmon
RUN pip install -e /salmon

RUN chmod +x /salmon/launch.sh
RUN chmod +rw /salmon
# ENTRYPOINT bash launch.sh
WORKDIR /salmon
CMD ["bash", "launch.sh"]
