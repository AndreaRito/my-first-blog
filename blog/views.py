from django.shortcuts import render

#Creiamo una vista come suggerisce il commento
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    
#abbiamo creato una funzione (def) chiamata post_list 
# che prende request e restituisce return una funzione
#  render che renderizza (mette insieme) il nostro
#  template blog/post_list.html.

