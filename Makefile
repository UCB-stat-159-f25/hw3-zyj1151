ENV_NAME = LOSC_env
ENV_FILE = environment.yml

env:
	if conda env list | grep -q "^$(ENV_NAME)\s"; then \
		conda env update -n $(ENV_NAME) -f $(ENV_FILE) --prune; \
	else \
		conda env create -n $(ENV_NAME) -f $(ENV_FILE); \
	fi

html:
	myst build --html

clean:
	rm -rf _build figures audio