FROM aborilov/django-backend
RUN apt-get update && apt-get install -y --no-install-recommends binutils libproj-dev gdal-bin && rm -rf /var/lib/apt/lists/*
ADD requirements.txt /code/
RUN pip install -r requirements.txt
