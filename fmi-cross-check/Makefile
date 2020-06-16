
# Remove "OMCompiler " and replace "~" with "-"
OMC_VERSION=$$(omc --version | sed -e 's/[\~]/-/g' | grep -oE '[^ ]+$$')
BRANCH_NAME=add-OpenModelica-$(OMC_VERSION)

all:
	make checkout-git
	make compile-OpenModelica-FMUS
	make validate-files

validate-files:
	python3 -m fmpy.cross_check.validate_vendor_repo

compile-OpenModelica-FMUS:
	omc buildFMUs.mos

checkout-git:
	echo OMC_VERSION: $(OMC_VERSION)
	git checkout master --force
	git branch -D $(BRANCH_NAME) || echo Already clean branches
	git checkout -b $(BRANCH_NAME)
