# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
# SPHINXBUILD   = python -msphinx
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Notarzttraining
SOURCEDIR     = .
# GITBRANCH := $(shell git rev-parse --abbrev-ref HEAD)
# BUILDDIR      = "$(HOME)"/Export/21-Notarzt-Sphinx-"$(GITBRANCH)"
# BUILDDIR      = _build/"$(GITBRANCH)"
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
