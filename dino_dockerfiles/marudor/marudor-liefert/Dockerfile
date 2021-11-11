FROM python:alpine

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY bot.py decorators.py models.py tools.py /app/
COPY handlers /app/handlers


ENTRYPOINT ["python", "bot.py"]
