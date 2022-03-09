IDE: PyCharm 2018.3.2. Community Edition
Required packages/libraries: listed in Requirements.txt

Reporting: testsuite/report.html - generated each time pytest runs (pytest.ini)

Manual testcases for screenshots: manual_testcases/test_ui_knime.txt
Defect reports: Defects/

automated testscases:
testsuite/test_rest_knime_hub.py  -corresponding feature file: testsuite/features/rest_knime_hub.feature
testsuite/test_ui_knime_hub.py

About pytest and feature files: Gherkin - BDD
https://pytest-html.readthedocs.io/en/latest/
https://pypi.org/project/pytest-bdd/



BEFORE RUNNING:
Configuring execution: based on pycharm-pytest-running-config.jpg
install packages based on Requirements.txt
change variables:
conftest.py
- token is saved here, that needs to be updated
- chrome_driver location must be changed to where you saved it locally


