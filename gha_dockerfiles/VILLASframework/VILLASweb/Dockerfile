 #
 # This file is part of VILLASweb.
 #
 # VILLASweb is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
 #
 # VILLASweb is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with VILLASweb. If not, see <http://www.gnu.org/licenses/>.
 # ******************************************************************************

FROM node:16.5 AS builder

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# use changes to package.json to force Docker not to use the cache
# when we change our application's nodejs dependencies:
ADD package.json /usr/src/app
RUN npm install --force

# Install app dependencies
ARG REACT_APP_BRAND
COPY . /usr/src/app
RUN npm run build

FROM nginx

COPY --from=builder /usr/src/app/build /usr/share/nginx/html
