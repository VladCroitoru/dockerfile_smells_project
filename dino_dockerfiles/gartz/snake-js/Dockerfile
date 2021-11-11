FROM node:carbon

# Define the folder where we will be running commands in the container
WORKDIR /frontend

ENV NODE_ENV=development

# Install the dependencies
COPY . .

RUN npm install \
    && NODE_ENV=production npm run build -- --mode=${NODE_ENV}

FROM progrium/busybox
LABEL maintainer="Gabriel Reitz Giannattasio <g@gartz.me>"

RUN opkg-install uhttpd
RUN printf '#!/bin/sh\nset -e\n\nchmod 755 /www\nexec /usr/sbin/uhttpd $*\n' > /usr/sbin/run_uhttpd && chmod 755 /usr/sbin/run_uhttpd

# Define the folder where we will be running commands in the container
WORKDIR /www

# Install the dependencies
COPY --from=0 /frontend/dist .

# Expose the project in the port 80
EXPOSE 80

# Start the development server in the port 80
ENTRYPOINT /usr/sbin/run_uhttpd -f -p 80 -h /www

