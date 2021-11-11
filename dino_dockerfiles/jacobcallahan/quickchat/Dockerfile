FROM python
MAINTAINER https://github.com/JacobCallahan

RUN apt-get update && apt-get install -y sqlite

COPY / /quickchat
WORKDIR /quickchat

RUN pip install -r requirements.txt && python dbinit.py

CMD python app.py
