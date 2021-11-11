FROM python:3.8
COPY . /komodo
WORKDIR /komodo
RUN pip install -r requirements.txt
CMD [ "python","-u", "./process.py" ]