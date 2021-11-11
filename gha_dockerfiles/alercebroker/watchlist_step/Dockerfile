FROM python:3.6

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app
COPY . /app

WORKDIR /app/scripts

CMD ["python", "run_step.py"]