ge_dict = {'Health_Proficiency': {'course': 'CDEC 161', 'units': 3.0}, 'Nat_Sci': {'course': 'ANTH 115', 'units': 3.0}, 'Beh_Sci': {'course': 'CD 110', 'units': 3.0}}
print(ge_dict)

# float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
proficiencies = ['Health_Proficiency']

# ge_list = {k: for (k) in ge_dict.items() if not in proficiencies}
ge_list = [ge_dict[x]['course'] for x in ge_dict if x not in proficiencies]
# ge_list = {v['course'] for v in ge_dict.items() if not k in proficiencies}

# for v in ge_dict.values():
#     print(v)


print(ge_list)