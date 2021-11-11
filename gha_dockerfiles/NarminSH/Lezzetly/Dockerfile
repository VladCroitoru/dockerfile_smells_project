FROM python:3.9

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000",  "lezzetly.wsgi"  ]