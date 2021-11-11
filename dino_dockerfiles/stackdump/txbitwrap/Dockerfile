FROM python:2.7.14

# prereqs 
WORKDIR /opt/txbitwrap
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# application
COPY . .
RUN pip install .

EXPOSE 8080

ENTRYPOINT ["./entry.sh"]
