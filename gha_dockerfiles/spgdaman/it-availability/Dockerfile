FROM python:3.7

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8892

COPY . .

CMD streamlit run --server.port 8892 app.py