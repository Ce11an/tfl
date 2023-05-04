# How to contribute
We welcome contributions to this project. There are many ways to contribute, from writing new features, to reporting
bugs.

Please use GitHub issues to report all bugs. You can also use the issues to ask questions, or request new features.

We use pull requests for all contributions. If you are not familiar with GitHub pull requests, please read
["Creating a pull request"](https://help.github.com/articles/creating-a-pull-request/) on GitHub's website for more
information.

## Contributing code

### Dependencies
We use [Poetry](https://python-poetry.org/) to manage dependencies. Please install Poetry before contributing code.
We also utilise [pre-commit](https://pre-commit.com/) to manage pre-commit hooks. Please install pre-commit before
contributing code.

You can install all dependencies by running `poetry install` in the root directory of this project.

### Code style
We use [black](https://black.readthedocs.io/en/stable/) to format our code as well as [ruff](https://beta.ruff.rs/docs/)
to lint our code. Please run `pre-commit run --all-files` before submitting a pull request to ensure your code is
formatted correctly and passes all linting checks.

### Testing
We use [pytest](https://docs.pytest.org/en/stable/) to test our code. Please write tests for all new code you write.
You can run all tests by running `pytest` in the root directory of this project.

## Contributing to documentation
We welcome contributions to our documentation. You can find the documentation in the `docs` directory. We use
[mkdocs](https://www.mkdocs.org/) to build our documentation. You can run `mkdocs serve` in the root directory of this
project to serve the documentation locally.

## Before submitting a pull request
Before submitting a pull request, please ensure that you have run `pre-commit run --all-files`, `pytest`, amd `mypy` to
ensure your code is formatted correctly, passes all linting checks, and passes all tests.

Please ensure you follow these steps:
1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Help
The [Makefile](Makefile) contains some useful commands to help you get started. You can run `make help` to see a list
of all available commands.

If you need help, please feel free to reach out to us!
