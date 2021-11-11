FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

CMD [ "python", "-m", "starpicker.run" ]
