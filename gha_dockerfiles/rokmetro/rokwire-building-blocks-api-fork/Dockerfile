#  Copyright 2020 Board of Trustees of the University of Illinois.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

FROM swaggerapi/swagger-ui:v3.28.0

COPY appconfigservice/appconfig.yaml /usr/share/nginx/html/app/
COPY authservice/auth.yaml /usr/share/nginx/html/app/
COPY eventservice/events.yaml /usr/share/nginx/html/app/
COPY profileservice/profile.yaml /usr/share/nginx/html/app/
COPY loggingservice/logging.yaml /usr/share/nginx/html/app/

ENV URLS "[{url: 'app/appconfig.yaml', name: 'App Config Building Block'}, {url: 'app/auth.yaml', name: 'Authentication Building Block'}, {url: 'app/events.yaml', name: 'Events Building Block'}, {url: 'app/profile.yaml', name: 'Profile Building Block'}, {url: 'app/logging.yaml', name: 'Logging Building Block'}, {url: 'https://api.rokwire.illinois.edu/health/doc', name: 'Health Building Block'}, {url: 'https://api.rokwire.illinois.edu/talent-chooser/doc', name: 'Talent Chooser Building Block'} ]"

VOLUME /usr/share/nginx/html/app/

ENV BASE_URL="/docs"

CMD ["sh", "/usr/share/nginx/run.sh"]
