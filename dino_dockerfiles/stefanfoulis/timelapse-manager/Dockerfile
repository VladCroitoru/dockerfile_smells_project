FROM stefanfoulis/timelapse-manager:1.8.0

COPY . /app
# gzip does not seem to work with python3 yet
ENV DISABLE_GZIP=True

RUN DJANGO_MODE=build python manage.py graphql_schema
RUN npm run build-production
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
