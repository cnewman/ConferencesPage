import json
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

class Conference:
	def __init__(self):
		self.confName = ""
		self.confDate = ""
		self.confLoc = ""
		self.abstrDate = ""
		self.pprDate = ""
		self.linkName = ""
		self.confStatus = ""

def GenerateConfPage(request):
	json_data=open('conferences.json')
	data = json.load(json_data)
	conflist = list()
	for ka, va in data.iteritems(): #iterate each conference list
		for kb, vb in va.iteritems(): #iterate each conference in the list
			for vc in vb: #iterate each list of items for the conference
				var = Conference()
				for keyval, datum in vc.iteritems(): #iterate each datum in the list for each conference
					if keyval == "confname":
						var.confName = datum
					elif keyval == "location":
						var.confLoc = datum
					elif keyval == "confdate":
						var.confDate = datum
					elif keyval == "abstractdate":
						var.abstrDate = datum
					elif keyval == "paperdate":
						var.pprDate = datum
					elif keyval == "linkname":
						var.linkName = datum
					elif keyval == "confstatus":
						var.confStatus = datum
				conflist.append(var)

	#with open('data.json', 'w') as outfile:
	#	json.dump(conflist, outfile)
	t = get_template('test.html')
	html = t.render(Context({'conf_list': conflist}))
	return HttpResponse(html)