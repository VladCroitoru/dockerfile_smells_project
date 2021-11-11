FROM python:3.6

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		gcc \
		zlib1g-dev \
		libjpeg-dev \
	&& pip install pillow

RUN mkdir -p /code/media \
    && mkdir -p /code/processed 

COPY wolverinator.py /code
COPY media /code/media

ENV IMG_PATH /code/media/placeholder.png
ENV DEST_PATH /code/processed

CMD ["python", "/code/wolverinator.py"]