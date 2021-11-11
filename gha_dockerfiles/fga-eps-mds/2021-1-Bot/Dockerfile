FROM python:3.8-slim

ADD ./bot /app
ADD ./start_services.sh /app

RUN pip install --upgrade pip && \ 
    pip install --progress-bar off -r /app/requirements.txt

RUN python -m spacy download pt_core_news_sm

WORKDIR /app

USER root

ENTRYPOINT [  ]

RUN chmod +x /app/start_services.sh

CMD /app/start_services.sh