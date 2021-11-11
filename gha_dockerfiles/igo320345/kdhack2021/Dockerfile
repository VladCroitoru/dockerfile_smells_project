FROM python

WORKDIR /app 
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python main.py" ]