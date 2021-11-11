FROM python:3.8

RUN mkdir /app
RUN mkdir /app/cfg
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app

# New model added. WARNING: Batch App update must be synchronized.
RUN wget https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/v0.2/LaBSE.zip --no-verbose -P /tmp/
RUN unzip /tmp/LaBSE.zip -d /app/model

# Download the list of stopwords from github repository
RUN wget https://raw.githubusercontent.com/JuvenalDuarte/portuguese_stopwords/main/stopwords.txt --no-verbose -P /app/cfg

RUN rm -rf tmp

EXPOSE 5000

CMD gunicorn -c /app/gunicorn.conf.py main:application
