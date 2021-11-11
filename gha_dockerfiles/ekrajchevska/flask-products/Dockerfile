FROM python:3.8

WORKDIR /project    
# isto kako mkdir + cd project

# COPY requirements.txt /requirements.txt

COPY . .

# koga go RUN pred copy . . mi javuva eror: could not find requirements.txt no such file or dir

RUN pip install -r requirements.txt             

# ENTRYPOINT [ "bash", "docker-entrypoint.sh" ]

CMD [ "bash", "docker-entrypoint.sh" ]

# CMD ["gunicorn", "wsgi:app", "--bind", "localhost:5000", "--workers=1"]

# tip: requirements da se install pred copy (koga nemame promena vo libs, samo sme menuvale nekoj file)
