ROOT_LABEL = docker.openmodelica.org
DOCKER_BUILD_ARGS ?=

.PHONY: latest build-deps-1.21.0

latest: build-deps-1.16.4 build-deps-cmake-1.16.3
	@echo "Build all images currently used to build and test OpenModelica on Jenkins."

build-deps-1.21.0:
	docker build $(DOCKER_BUILD_ARGS) --tag $(ROOT_LABEL)/build-deps:v1.21.0 -f Dockerfile.build-deps-1.21.0 .
	@echo "Finished build $(ROOT_LABEL)/build-deps:v1.21.0"

build-deps-1.16:
	@echo "build-deps-1.16 doesn't exist, use target build-deps-1.16.2 instead"

build-deps-1.16.2:
  # The dockerfile is not a typo. It really is Dockerfile.build-deps-1.16 for 1.16.2
	docker build $(DOCKER_BUILD_ARGS) --build-arg REPO=ubuntu:bionic --tag $(ROOT_LABEL)/build-deps:v1.16.2 -f Dockerfile.build-deps-1.16 .
	@echo "Finished build $(ROOT_LABEL)/build-deps:v1.16.2."

build-deps-1.16.3: build-deps-1.16.2
	docker build $(DOCKER_BUILD_ARGS) --tag $(ROOT_LABEL)/build-deps:v1.16.3 -f Dockerfile.$@ .
	@echo "Finished build $(ROOT_LABEL)/build-deps:v1.16.3."

build-deps-1.16.4: build-deps-1.16.3
	docker build $(DOCKER_BUILD_ARGS) --tag $(ROOT_LABEL)/build-deps:v1.16.4 -f Dockerfile.$@ .
	@echo "Finished build $(ROOT_LABEL)/build-deps:v1.16.4."

build-deps-1.16.5: build-deps-1.16.4
	docker build $(DOCKER_BUILD_ARGS) --tag $(ROOT_LABEL)/build-deps:v1.16.5 -f Dockerfile.$@ .
	@echo "Finished build $(ROOT_LABEL)/build-deps:v1.16.5."

build-deps-cmake-1.16.3: build-deps-1.16.3
	docker build $(DOCKER_BUILD_ARGS) --tag $(ROOT_LABEL)/build-deps-cmake:v1.16.3 -f Dockerfile.$@ .
	@echo "Finished build $(ROOT_LABEL)/build-deps-cmake:v1.16.3."
