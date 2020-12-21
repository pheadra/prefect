import prefect

prefect.context.setdefault("secrets", {}) # to make sure context has a secrets attribute
prefect.context.secrets["GITHUB_ACCESS_TOKEN"] = "fcfd03a0197716a596505b12d315e097775e2bf9"
