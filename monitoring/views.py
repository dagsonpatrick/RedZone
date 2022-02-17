from django.shortcuts import render
from api.services import evento_service
from django.contrib.auth.decorators import login_required

@login_required()
def monitoring(request):

    collaborators_in_redzone = evento_service.collaborators_within_redzone()
    collaborators_out_redzone = evento_service.collaborators_outside_redzone()
    qtd_in = len(collaborators_in_redzone)
    qtd_out = len(collaborators_out_redzone)

    '''for coll in collaborators_in_redzone:
            #print(coll.collaborator.first_name)
            print('------------------------------------------')
            print("Nome Portal: " + coll.portal)
            print("Tag: " + coll.tag.description)
            print("Collaborator: " + coll.collaborator.first_name)
            print("Sentido: " + coll.sentido)
            print("Temperature: " + str(coll.temperature))
            print("Battery: " + str(coll.battery))
            print("Status: " + str(coll.status))
            print("Timestamp: " + str(coll.timestamp))'''

    return render(request, 'monitoring_red_zone.html', { 'qtd_in': qtd_in, 'qtd_out': qtd_out , 'colls_in_redzone': collaborators_in_redzone, 'colls_out_redzone' : collaborators_out_redzone })