FROM python:3.9-alpine

ARG buildDeps='g++ gnupg curl libffi-dev openssl-dev musl-dev cargo'

WORKDIR /usr/src/app

COPY . .

RUN apk update \
	&& apk add --no-cache $buildDeps gcc unixodbc-dev \
	&& pip3 install --no-cache-dir -r requirements/time_tracker_api/prod.txt \
	&& curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.5.2.1-1_amd64.apk \
	&& curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.5.2.1-1_amd64.apk \
	&& curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.5.2.1-1_amd64.sig \
	&& curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.5.2.1-1_amd64.sig \
	&& curl https://packages.microsoft.com/keys/microsoft.asc  | gpg --import - \
	&& gpg --verify msodbcsql17_17.5.2.1-1_amd64.sig msodbcsql17_17.5.2.1-1_amd64.apk \
	&& gpg --verify mssql-tools_17.5.2.1-1_amd64.sig mssql-tools_17.5.2.1-1_amd64.apk \
	&& apk add --no-cache --allow-untrusted msodbcsql17_17.5.2.1-1_amd64.apk \
	&& apk add --no-cache --allow-untrusted mssql-tools_17.5.2.1-1_amd64.apk \
	&& rm msodbcsql17_17.5.2.1-1_amd64.apk mssql-tools_17.5.2.1-1_amd64.apk msodbcsql17_17.5.2.1-1_amd64.sig mssql-tools_17.5.2.1-1_amd64.sig \
	&& apk del $buildDeps \
	&& rm -rfv /root/.cache/pip/* && \
find /usr/local \( -type d -a -name test -o -name tests \) -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rfv '{}' \+

ENV FLASK_APP time_tracker_api

EXPOSE 5000

CMD ["gunicorn", "-b 0.0.0.0:5000", "api:app"]
