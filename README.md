# ChatGPT Testing

Introduction
===
Analyze ChatGPT's codex to determine it's viability to identify code issues, fix and suggest fixes.


Tech stack
===
1. Python 3 preferable

2. `openai` package, install using `pip install openai`


Prerequisites
===
1. Registered`OpenAI` account, to use API using `OPENAI_API_KEY`

2. `OPENAI_API_KEY` is sourced from system's environment properties

	a. If on Windows, refer this [__link__](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html)

	b. If using \*NIX `env OPENAI_API_KEY = "<PROVIDE_YOUR_OPENAI_API_KEY HERE>"`


Steps
===
1. Change to `ChatGTP-Testing` folder for executing logic

2. Run using `python3 chatGTP_test.py`

3. If all the required prerequisites are set correctly then python program will start logging the question and respective responses inside `responses` folder for particular language in file named `response-{ISO8601 dateformat}.py`



Resources
---
- [OpenAI's API documentation](https://platform.openai.com/docs/api-reference/introduction)

- [OpenAI's Code models](https://platform.openai.com/docs/models/codex)