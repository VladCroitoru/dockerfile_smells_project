FROM node:12 as frontend

RUN mkdir /tmp/frontend
WORKDIR /tmp/frontend

# cache hack; fragile
COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build

# -----------------------------------------------------------------------------
FROM python:3.7 as backend

RUN mkdir /opt/cosri-patientsearch
WORKDIR /opt/cosri-patientsearch

ARG VERSION_STRING
ENV VERSION_STRING=$VERSION_STRING

# Copy front-end files built in previous stage
COPY --from=frontend /tmp/frontend/patientsearch/dist/ /opt/cosri-patientsearch/patientsearch/static/

ENV FLASK_APP=patientsearch:create_app

# cache hack; very fragile
COPY requirements.txt ./
RUN pip install --requirement requirements.txt

COPY . .

CMD gunicorn --bind "0.0.0.0:${PORT:-8000}" 'patientsearch:create_app()'

EXPOSE 8000
