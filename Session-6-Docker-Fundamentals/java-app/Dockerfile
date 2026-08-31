FROM eclipse-temurin:21-jdk AS build

WORKDIR /app
COPY HelloServer.java .
RUN javac HelloServer.java

FROM eclipse-temurin:21-jre

WORKDIR /app
COPY --from=build /app/HelloServer.class .

EXPOSE 8080

CMD ["java", "HelloServer"]
