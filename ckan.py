import ckanclient
import json

api_key='<your-api-key>'
base_location='http://thedatahub.org/api'

def get_pkg_tag(ckan, tag):
	pkgs = ckan.tag_entity_get(tag)
	i=0
	for pkg_name in pkgs:
		print "retrieving",i,len(pkgs),pkg_name
		yield get_pkg(ckan,pkg_name)
		i=i+1


def get_pkg(ckan, pkg_name):
	try:
		pkg=ckan.package_entity_get(pkg_name)
		return pkg['resources']
	except Exception as e:
		print "error", str(e)

def list_tags(ckan):
	return ckan.tag_register_get()

def write_pkgs(ckan, tag, type=['CSV','XLS']):
	resources = {}
	print "tag=",tag
	print "types=",type

	with open('ckan-'+tag+'.json', 'w+') as f:
		for resource in get_pkg_tag(ckan,tag):
			if resource is not None:
				for el in resource:
					format = el['format'] or ''
					mimetype = el['mimetype'] or ''
					if (any([t in format.upper() for t in type])
					 or any([t in mimetype.upper() for t in type])):
						id=el['id']
						url=el['url']
						print {id:url}
						resources[id]=url
		f.write(json.dumps(resources,indent=4))

if __name__ == "__main__":
	import sys
	if (len(sys.argv) != 3):
		print "Usage:",sys.argv[0],"<tag> <api_key>"
		sys.exit(1)
	else:
		tag=sys.argv[1]
		api_key=sys.argv[2]
		print "init:",base_location,api_key
		ckan=ckanclient.CkanClient(base_location,api_key)
		write_pkgs(ckan,tag)

