ARG PYTHON_VERSION=3.7-alpine

FROM python:${PYTHON_VERSION}

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]