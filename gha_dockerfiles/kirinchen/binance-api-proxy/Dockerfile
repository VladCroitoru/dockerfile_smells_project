FROM python:3.9.2
RUN pip install pipenv
#COPY Pipfile /tmp
#COPY Pipfile.lock /tmp


#RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
#RUN pip install -r /tmp/requirements.txt
COPY . /myapp
WORKDIR  /myapp
RUN pipenv install
#RUN pipenv shell
# RUN pip install /tmp/myapp
EXPOSE 5000
ENV FLASK_APP=main
ENV FLASK_ENV=development
CMD ["pipenv","run","flask","run","--host=0.0.0.0"]
