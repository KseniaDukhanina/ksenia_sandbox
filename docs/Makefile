.PHONY: help gettext update-translation build-all

help:
	@echo "Available commands:"
	@echo "  make gettext           - Extract translatable strings"
	@echo "  make update-translation - Update translation files"
	@echo "  make build-all         - Build all language versions"

gettext:
	sphinx-build -b gettext docs/ docs/locale/ru/LC_MESSAGES/
	cd ksenia-sandbox-eng && sphinx-build -b gettext docs/ docs/locale/en/LC_MESSAGES/

update-translation:
	sphinx-intl update -p docs/locale/ru/LC_MESSAGES/ -l en -d ksenia-sandbox-eng/docs/locale/
	sphinx-intl update -p ksenia-sandbox-eng/docs/locale/en/LC_MESSAGES/ -l ru -d docs/locale/

build-all:
	sphinx-build -b html -D language=ru docs/ _build/ru/
	sphinx-build -b html -D language=en ksenia-sandbox-eng/docs/ _build/en/
