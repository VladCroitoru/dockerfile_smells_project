FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /haemo_support_backend
WORKDIR /haemo_support_backend
COPY ./ /haemo_support_backend
RUN pip install pipenv
RUN pipenv install --system
EXPOSE 8000