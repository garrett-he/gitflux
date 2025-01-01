.DEFAULT_GOAL := help

.PHONY: help
help: ## show help information
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.PHONY: init
init: ## Initialize project
	pdm install
	pdm run pre-commit install

.PHONY: lint
lint: ## Code analyse and lint
	pdm run pylint src/ tests/

.PHONY: test
test: ## Run tests
	pdm run pytest --cov=src --cov-report=term-missing --cov-report=xml

.PHONY: tox
tox: ## Run tox
	pdm run tox

.PHONY: build
build: ## Build project
	pdm build

.PHONY: publish
publish: build ## Publish project
	pdm publish

.PHONY: codecov
codecov: ## Upload coverage.xml to codecov.com
	pdm run pytest --cov=src --cov-report=xml
	codecov

.PHONY: dist
dist:
	rm -rf ./dist
	pdm run pyinstaller git-timemachine.spec
	cp {CHANGELOG.md,COPYING,README.md} ./dist/

.PHONY: clean
clean: ## Clean up cache files
	find . -name '__pycache__' -type d | xargs rm -rf
	rm -rf .pytest_cache/ dist/ build/
	rm -f coverage.xml
