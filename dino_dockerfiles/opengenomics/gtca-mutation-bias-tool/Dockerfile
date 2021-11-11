FROM python:2.7.13

WORKDIR /opt
RUN mkdir /opt/bin
COPY ./gtca_mutation_bias.py /opt/bin
ENV PATH $PATH:/opt/bin
RUN chmod +x /opt/bin/gtca_mutation_bias.py
