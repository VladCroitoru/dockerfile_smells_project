FROM python:2.7

ENV PIP_REQUIRE_VIRTUALENV false

RUN pip install --no-deps argparse djangocms-installer six dj-database-url pytz tzlocal

RUN apt-get -y update && apt-get -y install git unzip
ADD requirements.txt /requirements.txt
RUN djangocms -m -r /requirements.txt -q -p /cms preview

RUN pip install --upgrade https://github.com/divio/djangocms-admin-style/archive/master.zip

ADD create-users /cms/create-users
RUN chmod +x /cms/create-users

WORKDIR /cms
ADD settings.py /cms/preview/settings.py
ADD template.html /cms/preview/templates/aldryn_faq/plugins/category_list.html
ADD template.html /cms/preview/templates/aldryn_faq/plugins/latest_questions.html
ADD template.html /cms/preview/templates/aldryn_faq/plugins/question_list.html
ADD template.html /cms/preview/templates/aldryn_faq/plugins/top_questions.html
ADD template.html /cms/preview/templates/aldryn_faq/plugins/most_read_questions.html
ADD template.html /cms/preview/templates/aldryn_jobs/plugins/categories_list.html
ADD template.html /cms/preview/templates/aldryn_jobs/plugins/latest_entries.html
ADD template.html /cms/preview/templates/aldryn_people/plugins/standard/people_list.html
ADD base.html /cms/preview/templates/base.html
RUN wget https://github.com/twbs/bootstrap/releases/download/v3.3.5/bootstrap-3.3.5-dist.zip -O /tmp/bootstrap.zip
RUN unzip /tmp/bootstrap.zip -d /cms/preview/static
RUN rm /tmp/bootstrap.zip
RUN mv /cms/preview/static/bootstrap-3.3.5-dist/* /cms/preview/static/
RUN rm -rf /cms/preview/static/bootstrap-3.3.5-dist

RUN python manage.py migrate

# XXX intellectronica 2015-11-26 This initial data was prepared with
# Django 1.7 and no longer works. Needs to be updated.
# ADD initial_data.json /cms/initial_data.json
# RUN python manage.py loaddata /cms/initial_data.json
RUN /cms/create-users
EXPOSE 80

CMD python manage.py runserver 0.0.0.0:80
