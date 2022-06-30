captured=tuple(['Pikachu','Abra','Pidgey','Eevee','Pidgey'])

no=captured.count("Pidgey")
print(captured)
print("There are",no,"Pidgeys captured!")

pokemon=input("Which Pokemon did you capture?")
if pokemon in captured:
    print("This Pokemon is already captured!")

count1=len(captured)

print("There are",count1,"Pokemons captured!")
my_set = set(captured)
no2 = len(my_set)
print("There are",no2," different Pokemons captured")