FROM python:3.5

RUN pip install Flask==0.11.1 pymongo==3.4.0
COPY ./ /code/

WORKDIR /code
EXPOSE 8000

CMD python app.py

