# Copyright 2017 Aleksei Balan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM tomcat:alpine

# change Tomcat default port to Eureka default, download and unpack
RUN sed -i 's/8080/8761/g' conf/server.xml &&\
  wget http://repo1.maven.org/maven2/com/netflix/eureka/eureka-server/1.8.4/eureka-server-1.8.4.war\
    -q -O webapps/eureka.war &&\
  mkdir -p webapps/eureka &&\
  unzip -q webapps/eureka.war -d webapps/eureka &&\
  rm webapps/eureka.war

COPY *.properties webapps/eureka/WEB-INF/classes/

COPY eureka-logo-150.png webapps/ROOT/favicon.ico

EXPOSE 8761

# Have fun
