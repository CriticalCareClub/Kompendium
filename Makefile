# -------- Minimal, DRY Makefile for Sphinx --------

# Configurable vars (overridable via CLI: make SPHINXOPTS="-W")
SPHINXBUILD ?= sphinx-build
SPHINXPROJ  ?= KS_HY_007_Hygienekodex
SOURCEDIR   ?= Text
SPHINXOPTS  ?= #  = -W
EXTRAOPTS   ?=             # put additional options here if needed

# Branch-aware build dir (fallback to 'nogit' if outside a git repo)
GITBRANCH := $(shell git rev-parse --abbrev-ref HEAD 2>/dev/null || echo nogit)
BUILDDIR  ?= Export/$(GITBRANCH)

# Default target shows Sphinx's own help
.PHONY: help
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

# ---------- HTML builders ----------
# Usage: make html-draft | html-sprint | html-review | html-final
# Alias: make html  -> html-final
.PHONY: html html-%
html-%:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) --tag $* $(EXTRAOPTS)
html: html-final

# ---------- LaTeX builders (source only) ----------
# Usage: make latex-draft | latex-sprint | latex-review | latex-final
# Alias: make latex -> latex-final
.PHONY: latex latex-%
latex-%:
	@$(SPHINXBUILD) -M latex "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) --tag $* --tag letter $(EXTRAOPTS)
latex: latex-final

# ---------- PDF builders (latexpdf) ----------
# Usage: make pdf-draft | pdf-sprint | pdf-review | pdf-final
# Alias: make pdf -> pdf-final
.PHONY: pdf pdf-%
pdf-%:
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) --tag $* --tag letter $(EXTRAOPTS)
pdf: pdf-final

# ---------- Print builders (same as pdf for convenience) ----------
# Usage: make print-draft | print-sprint | print-review | print-final
# Alias: make print -> print-final
.PHONY: print print-%
print-%:
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) --tag $* --tag a4 $(EXTRAOPTS)
print: print-final

# Catch-all: route unknown targets to sphinx-build -M
# (kept from your original; useful for e.g. 'make dirhtml', 'make linkcheck', etc.)
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
