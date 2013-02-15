ckan
====

some simple ckan tools

ckan.py - retrieves all CSV/XLS files from datahub.io CKAN repo with a given tag.

usage: python ckan.py <tag_name> <api_key>

it will output files of the form ckan-<tag_name>.json containing a JSON dict mapping CKAN resource ids to URLs.

