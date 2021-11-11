FROM python
ADD microblog /microblog
WORKDIR /microblog

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
