#Install Python/Debian OS
FROM python:3.7

#Set working directory as /app
WORKDIR /app

#Copy the content into /app
COPY . /app

#Install the requirements for OS and Python
RUN pip3 install -r ./requirements.txt

#Set streamlit app as default
CMD streamlit run --server.port $PORT app.py
