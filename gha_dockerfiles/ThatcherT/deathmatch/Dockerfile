FROM python:3.7.6
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get -y install cmake libopenmpi-dev python3-dev zlib1g-dev python3-opencv
RUN pip install -r requirements.txt --no-cache-dir
# Maybe this should only copy the parts that need to be on the running web server
COPY . /app/
# collectstatic will copy the staticfiles_src to staticfiles (published under /static)
RUN python manage.py collectstatic --noinput