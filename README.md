Yet Another DAta CAtalog

A static website as a data catalog. There is no need of a running back end database because the data is not frequently
modified and looks the same for all users.

Python package offers a CLI and an API to extract metadata from data assets (data warehouses, data lakes, Great
Expectation, OpenLineage, dashboarding tools).

Possible to extract metadata from a whole asset or restrict by schema, table, column, metadata type. Advantage: static
tables don't need to be inspected. Metadata extraction can be part of a data pipeline.

HTML files are generated as a result and can be hosted in cloud storage service for a serverless solution or in a
traditional web server

# Develop
Clone this repository, create and activate a virtual environment, and install the package with
```bash
pip install --editable .
```
Does the command below print the version without blowing up? Then congrats, you're good to go.