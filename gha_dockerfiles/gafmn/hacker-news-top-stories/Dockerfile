FROM apache/airflow:2.1.3-python3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src ./src

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow"
