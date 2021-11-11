FROM openjdk

WORKDIR /app

COPY target/api-product-0.0.1-SNAPSHOT.jar /app/api-product.jar

ENTRYPOINT ["java", "-jar", "api-product.jar"]