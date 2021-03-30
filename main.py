from models.address_builder import AddressBuilder

ab = AddressBuilder()
print(ab.__dict__)
adresse = ab.set_pays('France'). \
    set_code_postal(3555222)\
    .build()
# ab.voirie = 'rue henri '
# ab.numero = '19'

print(adresse)

# a = ab.pays("Algerie").build()

# print(str(a))
