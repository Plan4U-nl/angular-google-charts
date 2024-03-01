{
	"name": "plan4ucomponents-agendaview",
	"displayName": "agendaview",
	"version": 2,
	"definition": "plan4ucomponents/plan4ucomponents/agendaview.js",
	"libraries": [],
	"model": {
		"url" : {"type": "string", "default":"/"}
	},
	"handlers": {
		"viewAction": {
			"parameters":[
								{
						          "name":"event",
								  "type":"JSEvent"
								}
							 ]
		},
		"planAction": {
			"parameters":[
								{
						          "name":"event",
								  "type":"JSEvent"
								}
							 ]
		}
  }
}