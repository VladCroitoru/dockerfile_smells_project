FROM  continuumio/miniconda3

LABEL Author, Amine HadjYoucef
LABEL mantainer="wallison_93@hotmail.com"

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . $APP_HOME

#---------------- Prepare the envirennment
RUN /opt/conda/bin/conda install jupyter -y --quiet
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "./docker_entrypoint.sh" ]
