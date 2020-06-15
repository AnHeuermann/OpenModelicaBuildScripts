
OMC_VERSION=$$(omc --version | grep -oE '[^ ]+$$'| grep -o '^[^+]*')
BRANCH_NAME=add-OpenModelica-$(OMC_VERSION)



all: validate-files

validate-files: compile-OpenModelica-FMUS
	python3 -m fmpy.cross_check.validate_vendor_repo

compile-OpenModelica-FMUS: checkout-git
	omc buildFMUs.mos

checkout-git:
	echo OMC_VERSION: $(OMC_VERSION)
	git checkout master --force
	git branch -D $(BRANCH_NAME) || echo Already clean branches
	git checkout -b $(BRANCH_NAME)
