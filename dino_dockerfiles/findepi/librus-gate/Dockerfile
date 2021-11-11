FROM python:3

COPY *py requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 8723
CMD ["gunicorn", "--bind", "0.0.0.0:8723", "main:app"]
