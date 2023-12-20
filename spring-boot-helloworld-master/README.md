# 1. what are the core Devops responsibilties we normally carry?

Devops teams comprise of the role Development and Operations
Some keys are:
* CI/CD
* Automated
* Version Control management
* Culture of trust in team
* Adaptability
* Quality Assurance
* Security
* Infrastrucutre Specialist/Cloud Architect
* Feedback


# 2. Explain the concept of Git Flow using diagram

**Git WorkFlow**

![Git WorkFlow](https://i1.wp.com/iot4beginners.com/wp-content/uploads/2020/05/Screenshot-134.png?fit=1024%2C629&ssl=1)

* **Working Directory:** 

    It is where developer/User working on the files in their local machine

    *Working Directory to Staging Area*

    The add command stages content from the working directory to the staging area. Contrary to what the name implies, you always use the git add command to stage anything, even content that is not new and that has been staged before.

* **Staging Area**

    To stage a file is to prepare it for a commit. Because git exposes this action to the users control it allows you to create partial commits, or to modify a file, stage it, modify it again, and only commit or revert to the original modification. Staging allows you finer control over exactly how you want to approach version control.

    *Staging Area to Local Repository*

    The command that is used to promote things from the staging area to the local repository is the git commit command. Think of it as making a commitment to put your changes into the official source management repository. This is most similar to what you might see as check-in in other source management systems, but note that it only takes content from the staging area.

* **Remote Repository**

    Remote is actual repository providers like github, bitbucket, Azure Repo, Google cloud Repository, etc

    *Local Repository to Remote Repository*

    To synchronize changes from a local repository to the corresponding remote repository, the command is git push. Unlike commits into the local repository, merge conflicts from content pushed by other users can be encountered here. Also, being able to push to a particular remote repository assumes appropriate access and permissions via whatever protocol and permissions checking is being used.


# 3. CI/CD tools makes integration and deployment

__Building the code by using docker to make image to run as container in Kubernetes__

Creating Dockerfile to give the steps to build the image from the code

*Dockerfile*

```
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

```

__Using Azure pipeline to Build and push the code in DockerHub Repositries__

*Azure-Pipeline.yml*

```
# Docker
# Build a Docker image
# https://docs.microsoft.com/azure/devops/pipelines/languages/docker

trigger:
- master

resources:
- repo: self

variables:
  tag: '$(Build.BuildId)'
  imageName: spring-hello

stages:
- stage: Build
  displayName: Build image
  jobs:
  - job: Build
    displayName: Build
    pool:
      vmImage: ubuntu-latest
    steps:
    - task: Docker@2
      displayName: Build an image
      inputs:
        containerRegistry: 'DockerHub'
        repository: '$(imageName)'
        command: 'build'
        Dockerfile: '**/Dockerfile'
        tags: '$(tag)'
    - task: Docker@2
      inputs:
        containerRegistry: 'DockerHub'
        command: 'push'

```

__Using K8s manifest to dpeloy the dockerized application in the cluster and accessing using the service__

*deployment.yml*

```
apiVersion: apps/v1
kind: Deployment 
metadata: #Dictionary
  name: myapp-deployment
spec: # Dictionary
  replicas: 2
  selector:
    matchLabels:
      app: myapp
  template:  
    metadata: # Dictionary
      name: myapp
      labels: # Dictionary
        app: myapp  # Key value paids
    spec:
      containers: # List
        - name: myapp-container
          image: springhello
          ports: 
            - containerPort: 8080
    
```

*service.yml*

```
apiVersion: v1
kind: Service 
metadata:
  name: deployment-loadbalancer-service
spec:
  type: LoadBalancer # ClusterIp,# NodePort
  selector:
    app: myapp
  ports: 
    - name: http
      port: 8080 # Service Port
      targetPort: 8080 # Container Port

```

In existing k8s cluster use the command to deploy the defined application

```
kubectl apply -f deployment.yml
```

```
kubectl apply -f service.yml
```
_To list the service to access from public_
```
kubectl get svc  
```
_To list the running pods_

```
kubectl get pods
```
