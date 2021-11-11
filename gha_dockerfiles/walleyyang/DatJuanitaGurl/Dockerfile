FROM python:3.9-slim

# tzdata for timzone
RUN apt-get update -y
RUN apt-get install -y tzdata
 
# timezone env with default
ENV TZ America/New_York

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

WORKDIR src

CMD ["python", "main.py"]