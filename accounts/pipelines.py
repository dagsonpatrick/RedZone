from .models import Usuario
import urllib.request
import os
import uuid

def get_file_path(filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("foto_perfil/", filename)

def save_profile(backend, user, details, response, **kwargs):

    if backend.name == "google-oauth2":

        profile = user
        if profile is None:
            profile = Usuario(user.id)
        profile.first_name = details['first_name']
        profile.last_name = details['last_name']
        filename = details['first_name'] + details['last_name']
        filename = get_file_path(filename)
        urllib.request.urlretrieve(response['picture'], "media/{}.jpg".format(filename))
        profile.profile_picture = filename+".jpg"
        profile.save()

