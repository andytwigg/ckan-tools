ckan
====

some simple ckan tools

ckan.py - retrieves all CSV/XLS files from datahub.io CKAN repo with a given tag.

usage: python ckan.py <api_location> <tag_name> <api_key>

eg python ckan.py http://data.gov.uk/api weather $api_key

it will output files of the form ckan-<tag_name>.json containing a JSON dict mapping CKAN resource ids to URLs.

