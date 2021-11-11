FROM phirov/angular-quickstart

ADD app /app
ADD assets/sources.list /etc/apt

RUN apt-get update -y && \
	apt-get install vim -y && \
	apt-get clean -y

WORKDIR /app	
RUN cd /app	

RUN mkdir /app/node_modules
RUN cp -rf /usr/src/app/node_modules/* /app/node_modules

RUN npm install -g cnpm --registry=https://registry.npm.taobao.org

# install typescript
RUN cnpm install -g tslint typescript typings concurrently lite-server && \
    mkdir -p /workspace/build && \

    # clean-up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN cnpm install -g gulp 
RUN cnpm install gulp --save-dev
RUN cnpm install gulp-sass gulp-autoprefixer gulp-minify-css gulp-jshint gulp-concat gulp-uglify gulp-imagemin gulp-notify gulp-rename gulp-livereload gulp-cache --save-dev
RUN cnpm install --save-dev gulp-webserver  browser-sync  gulp-less gulp-tsc

RUN cnpm update