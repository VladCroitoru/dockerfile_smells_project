FROM java:7
COPY /src /src
COPY /lib /lib
RUN javac -cp lib/jedis-2.1.0-sources.jar -d . src/JavaRedisApp.java
