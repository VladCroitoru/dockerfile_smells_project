FROM python:3.8.10

ENV PYTHONUNBUFFERED 1
EXPOSE 8000

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

CMD  uvicorn --host=0.0.0.0 main:app --reload