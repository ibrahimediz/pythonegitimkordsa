import os
print(*os.listdir("/workspace/pythonegitimkordsa/Exercises"))
filename = "01_05_dict"
metin = """
var1 = '41,5,59,N'
"""
for item in os.listdir("/workspace/pythonegitimkordsa/Exercises"):
    with open(f"/workspace/pythonegitimkordsa/Exercises/{item}/{filename}.ipynb","a+") as dosya:
        pass
        # dosya.seek(0)
        # dosya.write(metin)

    
