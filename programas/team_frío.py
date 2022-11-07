"""
Programa que sugiera bebidas calientes y algún tipo de repostería para acompañarla.
"""
import random
print("¿Hace frío?, hay que beber algo calientito.\n")

beverages = ['té', 'capuchino', 'atole', 'chocolate abuelita', 'agua tibia', 'café negro']
desserts = ['bolillo', 'galletas María', 'pan tostado', 'pay', 'pastel']

for beverages in range (0,7):
 beverages = random.randint(1,6)
 print(beverages)