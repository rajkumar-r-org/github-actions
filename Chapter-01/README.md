##   Trigger the workflows based on the branch or Specific path


Events: Triggering the Workflow based on the branch and specific path in the repository

```yaml
on:
  push:
    branches:main
    paths:
    -'Chapter-01/**'
```

This will trigger the pipeline when push happened for the 'main' branch for the specific path in the repository.


Jobs:

We can one or more job and each job can have multiple steps

```yaml
jobs:
  run-shell-commands:
    runs-on: ubuntu-latest
    steps:
      - name: echo a string
        run: echo "Hello World"
      - name: Multiline Command
        run: |
          node -v
          npm -v
  parallel-job-macos:
    runs-on: macos-latest
    steps:
      - name: View SW Version
        run: sw_vers
  dependant-job:
    runs-on: windows-latest
    needs: run-shell-commands
    steps:
      - name: echo a string
        run: Write-Output "Windows String"
      - name: Final step
        run: Write-Output "Successfully completed"
```
