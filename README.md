**Understanding of GitHub Actions**

You can configure a GitHub Actions *workflow* to be triggered when an *event* occurs in your repository, such as a pull request being opened or an issue being created. Your workflow contains one or more *jobs* which can run in sequential order or in parallel. Each job will run inside its own virtual machine  *runner* , or inside a container, and has one or more *steps* that either run a script that you define or run an  *action* , which is a reusable extension that can simplify your workflow.

![Components](https://docs.github.com/assets/cb-25535/mw-1440/images/help/actions/overview-actions-simple.webp "Components of GitHub Action")

[Workflows](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#workflows)

A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.

Workflows are defined in the `.github/workflows` directory in a repository, and a repository can have multiple workflows, each of which can perform a different set of tasks. For example, you can have one workflow to build and test pull requests, another workflow to deploy your application every time a release is created, and still another workflow that adds a label every time someone opens a new issue.

[Events](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#events)

An event is a specific activity in a repository that triggers a workflow run. For example, activity can originate from GitHub when someone creates a pull request, opens an issue, or pushes a commit to a repository. You can also trigger a workflow to run on a [schedule](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule), by [posting to a REST API](https://docs.github.com/en/rest/repos#create-a-repository-dispatch-event), or manually.

[Jobs](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#jobs)

A job is a set of *steps* in a workflow that is executed on the same runner. Each step is either a shell script that will be executed, or an *action* that will be run. Steps are executed in order and are dependent on each other. Since each step is executed on the same runner, you can share data from one step to another. For example, you can have a step that builds your application followed by a step that tests the application that was built.

You can configure a job's dependencies with other jobs; by default, jobs have no dependencies and run in parallel with each other. When a job takes a dependency on another job, it will wait for the dependent job to complete before it can run. For example, you may have multiple build jobs for different architectures that have no dependencies, and a packaging job that is dependent on those jobs. The build jobs will run in parallel, and when they have all completed successfully, the packaging job will run.

[Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#actions)

An *action* is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task. Use an action to help reduce the amount of repetitive code that you write in your workflow files. An action can pull your git repository from GitHub, set up the correct toolchain for your build environment, or set up the authentication to your cloud provider.

You can write your own actions, or you can find actions to use in your workflows in the GitHub Marketplace.

[Runners](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#runners)

A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows; each workflow run executes in a fresh, newly-provisioned virtual machine. GitHub also offers larger runners, which are available in larger configurations. For more information, see "[About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners)." If you need a different operating system or require a specific hardware configuration, you can host your own runners.

[Create an example workflow](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#create-an-example-workflow)

GitHub Actions uses YAML syntax to define the workflow. Each workflow is stored as a separate YAML file in your code repository, in a directory named `.github/workflows`.

You can create an example workflow in your repository that automatically triggers a series of commands whenever code is pushed. In this workflow, GitHub Actions checks out the pushed code, installs the [bats](https://www.npmjs.com/package/bats) testing framework, and runs a basic command to output the bats version: `bats -v`.

1. In your repository, create the `.github/workflows/` directory to store your workflow files.
2. In the `.github/workflows/` directory, create a new file called `learn-github-actions.yml` and add the following code.
3. Commit these changes and push them to your GitHub repository.

```yaml
name: learn-github-actions
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v3
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v

```

[Visualizing the workflow file]()

![Visualize](https://docs.github.com/assets/cb-62091/mw-1440/images/help/actions/overview-actions-event.webp "Visualizing the workflow file")
