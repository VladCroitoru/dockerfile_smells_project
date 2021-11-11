FROM python:alpine
RUN apk --update add git gcc musl-dev 
RUN pip3 install pew
RUN pew new -d --python=python3 FFA_JOBS_SETTINGS

# pytz: for queryset filter in openCasesSameDate
RUN pew in FFA_JOBS_SETTINGS pip install Django pytz django_filter

EXPOSE 8000
WORKDIR /usr/share/ffa-jobs-settings
COPY . .

COPY docker-entry.sh /usr/bin/
RUN chmod +x /usr/bin/docker-entry.sh



ENTRYPOINT docker-entry.sh
