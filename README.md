graphql-template
===============

This repository is a template for Python project to build a GraphQL server.
You can use this template to create a new Python project with the following features:

- `strawberry` for GraphQL server
- `poetry` for dependency/requirements management and virtual environment setup
- `pytest` configuration for testing
- `black` configuration for linting
- `click` for command line interface
- `loguru` for logging setup at different levels
- `Dockerfile` and `docker-compose` setup for containerization
- `Makefile` with common tasks

Run
---

To run the GraphQL server, use the following command:

```bash
make lint test # Perform linting and test
make run
```

![Run Command](https://i.imgur.com/o99zwW1.png)

### GraphQL IDE Dashboard

This project is using the [strawberry](https://github.com/strawberry-graphql/strawberry) python library for GraphQL server which comes with [GraphQL/GraphIQL](https://github.com/graphql/graphiql) dashboard.
After running the server as shown above, go to the following URI in your browser:
`http://127.0.0.1:8000/graphql`

![GraphiQL Dashboard](https://i.imgur.com/qqdZIAz.png)


You can find more useful commands in the `Makefile`.



Installation
------------

To create a new project using this template, run the following command:

```bash
export APP_NAME=my-new-app
git clone --recursive https://github.com/ylogx/graphql-template.git ${APP_NAME} && cd ${APP_NAME} && bin/new-project
```

This will clone the repository and setup code for your new specified App Name.
This will install dependencies and setup a virtual environment for the project.
You can use `poetry` commands to manage dependencies and virtual environment.

Here's how the installation looks like:

![Installation Screenshot](https://i.imgur.com/npEvTcu.png)
