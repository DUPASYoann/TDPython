# Python TP8

## Tester un calcul (style calcul_long ci-dessous) avec du multi-threading et du multi- processing en observant l’utilisation des coeurs de votre CPU.

**Code**

>        import threading
>        
>        class SummingThread(threading.Thread):
>             def __init__(self,min,max):
>                 super(SummingThread, self).__init__()
>                 self.min=min
>                 self.max=max
>        
>        
>             def run(self):
>                 while self.max>self.min :
>                     self.max-=1
>        
>        
>        thread1 = SummingThread(0,1E7/2)
>        thread2 = SummingThread(0,1E7/2)
>        thread1.start()
>        thread2.start()
>        thread1.join()
>        thread2.join()
>        result = thread1.max + thread2.max
>        print (result)

Le programme ci dessus sépare le calcul en deux 2 et l'effectue dans 2 threads différents.
## Faire un programme qui construit et affiche une peinture avec des fourmis. Les paramètres (page 205 du pdf) seront à mettre dans un fichier texte ou mieux XML. En plus de dessiner une jolie peinture, l’objectif est de mettre en oeuvre la programmation asynchrone.

NON TERMINE