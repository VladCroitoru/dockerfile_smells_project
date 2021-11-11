FROM python:3.8.5
WORKDIR /streamlit_app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5432

COPY . /streamlit_app/

CMD streamlist run --server.port 5432 --server.enableCORS false streamlit_app.py

