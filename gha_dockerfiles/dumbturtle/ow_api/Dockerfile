FROM python:slim

RUN useradd api_app

WORKDIR /home/api_app
COPY . /home/api_app

RUN python -m pip install --no-cache-dir -r requirements.txt

RUN chown -R api_app:api_app /home/api_app
USER api_app

RUN python create_db.py
EXPOSE 5000
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]