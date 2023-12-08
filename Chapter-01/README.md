**Basic Workflow**

Triggering the Workflow based on the branch and specific path in the repository

on:
  push:
    branches:main
    paths:
    -'Chapter-01/**'

This will trigger the pipeline when push happened for the 'main' branch for the specific path in the repository.
