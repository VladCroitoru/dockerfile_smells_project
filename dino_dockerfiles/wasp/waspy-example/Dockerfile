FROM python:3.6

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r /app/requirements.txt

COPY . /app/

CMD ["python3", "/app/run.py"]
