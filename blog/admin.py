from django.contrib import admin
from .models import Post

admin.site.register(Post)



#Come puoi vedere, stiamo importando (include) il
# modello di Post che abbiamo definito nel capitolo
#  precedente. Per far si che il nostro modello sia
#  visibile nella pagina di admin, dobbiamo registrare 
# questo modello con admin.site.register(Post).