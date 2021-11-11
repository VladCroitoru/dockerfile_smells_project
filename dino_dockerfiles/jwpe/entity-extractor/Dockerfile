FROM trackmaven/nltk
MAINTAINER Jonathan Evans "jon@trackmaven.com"

RUN pip install requests beautifulsoup4 numpy flask flask_nicely

ADD entity_extractor /home/app

WORKDIR /home/app

EXPOSE 5000

CMD python main.py