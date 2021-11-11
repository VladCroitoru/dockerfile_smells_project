FROM python:2-alpine
COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
CMD python /app/main.py
