FROM maven:3.6.3 as builder
RUN mkdir -p /app/source
COPY . /app/source
WORKDIR /app/source
RUN mvn package


FROM adoptopenjdk/openjdk11:alpine-jre
ARG JAR_FILE=springhello.jar
WORKDIR /opt/app

COPY --from=builder /usr/src/app/target/${JAR_FILE} /opt/app/
EXPOSE 8080
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom", "-jar", "/app/app.jar"]