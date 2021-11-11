FROM python:3.8

RUN apt install libpq-dev

RUN pip install wheel --upgrade

RUN pip install uvicorn aiofiles 'wf-fastapi-auth0>=1.0.2' 'python-jose>=3.3.0' 'fastapi>=0.68' 'auth0-python>=3.16.2' 'cachetools>=4.2.2' 'sqlalchemy>=1.4.23' 'psycopg2>=2.9.1' 'pydantic[email]'

RUN mkdir -p /app

WORKDIR /app


COPY multiview_stream_service/ /app/multiview_stream_service/
COPY setup.py /app/setup.py

RUN pip install -v -e .

CMD python -m multiview_stream_service
