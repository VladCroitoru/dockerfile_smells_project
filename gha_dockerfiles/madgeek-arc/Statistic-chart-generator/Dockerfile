from ubuntu:18.04

run apt update
run apt install -y maven openjdk-8-jdk git

run update-java-alternatives --set java-1.8.0-openjdk-amd64

workdir /usr/local/app

copy pom.xml .
copy ./Application/pom.xml ./Application/pom.xml
copy ./ChartDataFormatter/pom.xml ./ChartDataFormatter/pom.xml
copy ./DBAccess/pom.xml ./DBAccess/pom.xml

run mvn dependency:go-offline 

copy ./Application/src ./Application/src
copy ./ChartDataFormatter/src ./ChartDataFormatter/src
copy ./DBAccess/src ./DBAccess/src

run mvn clean package  -DskipTests

run git clone -c http.sslVerify=false https://code-repo.d4science.org/antonis.lempesis/stats-tool-configuration.git
run mkdir -p /var/lib/tomcat8/lib/statsConfig
run cp /usr/local/app/stats-tool-configuration/madgik/* /var/lib/tomcat8/lib/statsConfig

ENTRYPOINT ["java","-jar","Application/target/Statistic-chart-generator-Application-0.0.1-SNAPSHOT.war","--server.port=8180","--spring.config.location=file:/var/lib/tomcat8/lib/statsConfig/", "--spring.redis.host=esperos.di.uoa.gr"]
