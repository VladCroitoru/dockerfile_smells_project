FROM python:3.6.0

COPY ./app /app
COPY ./wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py
