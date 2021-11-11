# WSO2 Enterprise Integrator Docker Image
#
# License: GNU Lesser General Public License (LGPL), version 3 or later
# See the LICENSE file in the root directory or <http://www.gnu.org/licenses/lgpl-3.0.html>.

FROM alpine AS builder

WORKDIR /opt

ARG EI_VERSION=6.6.0
ARG PRODUCT_NAME=wso2ei
ARG ZIP_URL=https://product-dist.wso2.com/products/enterprise-integrator/$EI_VERSION/$PRODUCT_NAME-$EI_VERSION.zip

RUN apk add --update curl unzip; \
  curl -LOk -A "testuser" -e "http://connect.wso2.com/wso2/getform/reg/new_product_download" $ZIP_URL; \
  unzip -qq $PRODUCT_NAME-$EI_VERSION.zip; \
  mv $PRODUCT_NAME-$EI_VERSION $PRODUCT_NAME; \
  rm -f $PRODUCT_NAME/bin/*.bat; \
  rm -f wso2*.zip

FROM openjdk:11-jre
LABEL maintainer="Bruno Silva <bruno@modoagil.com.br>"

COPY --from=builder /opt /opt

ENV EI_HOME /opt/wso2ei
ENV PATH $PATH:$EI_HOME/bin:$JAVA_HOME/bin
ENV JAVA_OPTS "$JAVA_OPTS -XX:+UnlockExperimentalVMOptions -XX:+UseZGC"

WORKDIR /

EXPOSE 8280 8243 9443

ENTRYPOINT ["integrator.sh"]
