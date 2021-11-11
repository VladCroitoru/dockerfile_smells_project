FROM python:3.8

COPY techtrends/ /techtrends
WORKDIR /techtrends

RUN pip install -r requirements.txt && python init_db.py

EXPOSE 3111

CMD ["python", "app.py", "--host=0.0.0.0"]
