FROM node:8
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install gcc autoconf libpng-dev
RUN npm config set unsafe-perm=true
RUN npm install -g \
  webpack@4.18.0 \
  webpack-dev-server@3.1.8 \
  copy-webpack-plugin@4.5.2 \
  extract-text-webpack-plugin@3.0.2 \
  css-loader@1.0.0 \
  style-loader@0.23.0 \
  node-sass@4.9.3 \
  sass-loader@7.1.0 \
  sass-resources-loader@1.3.3 \
  imagemin \
  imagemin-optipng \
  imagemin-svgo \
  imagemin-gifsicle \
  imagemin-mozjpeg@7.0.0 \
  imagemin-jpegoptim@5.2.0 \
  imagemin-jpeg-recompress@5.1.0 \
  imagemin-pngquant \
  imagemin-webpack-plugin@2.2.0 \
  webpack-manifest-plugin@2.0.3
RUN npm rebuild node-sass
