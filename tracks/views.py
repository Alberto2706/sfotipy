import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Track

# Ccreate your views here.
def track_view(request, title):
	#try:
	#	track = Track.objects.get(title=title)
	#except Track.DoesNotExist:
	#	raise Http404

	track = get_object_or_404(Track, title=title)
	bio= track.artist.biography

	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album.title,
		'artist': {
			'name': track.artist.first_name,
			'bio': bio,
		}
	}
	#convertir de diccionario a json
	json_data = json.dumps(data)

	#convertir de json a diccionario
	#dic = json.loads(string_json)

	return HttpResponse(json_data, content_type='application/json')
	#return render(request, 'track.html',{'track':track, 'bio': bio})
