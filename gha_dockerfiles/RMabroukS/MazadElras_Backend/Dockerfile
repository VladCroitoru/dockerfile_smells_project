FROM python

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code

COPY requirements.txt /code/
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code

RUN python manage.py check
RUN python manage.py collectstatic --no-input

# ADD migrate-data.sh /code/
# RUN chmod +x migrate-data.sh
# RUN chown -R www-data:www-data /code/
# RUN sed -i 's/\r$//g' /code/migrate-data.sh
CMD [ "/code/migrate-data.sh" ]
# RUN python manage.py migrate

# (gunicorn bookingsystem.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3)
CMD ["gunicorn", "--workers", "3", "--user", "www-data", "--bind", "0.0.0.0:8000", "--chdir", "ads_app", "ads_app.wsgi:application"]
