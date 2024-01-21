.venv/bin/ruff check --fix --force-exclude --exit-non-zero-on-fix $@
.venv/bin/ruff format --check --force-exclude $@
