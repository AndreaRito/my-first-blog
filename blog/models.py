from django.conf import settings 
from django.db import models 
from django.utils import timezone 


class Post(models.Model): #models.Model ignifica che 
    #il Post è un modello Django, quindi Django sa 
    # #che dovrebbe essere salvato nel database.
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     #models.ForeignKey - questo è un link a un altro modello.
     title = models.CharField(max_length=200)
     #models.CharField - così si definisce un testo con un numero limitato di lettere.
     text = models.TextField()
     #models.TextField - questo è il codice per definire un testo senza un limite. Sembra l'ideale per i contenuti di un post, vero?
     created_date = models.DateTimeField(default=timezone.now)
     #models.DateTimeField - questo per la data ed l'ora.
     published_date = models.DateTimeField(blank=True, null=True)

     def publish(self): #metodo pubblicare
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.title
         
