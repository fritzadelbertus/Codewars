# Codewars: Pete, the Baker
# Source: https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
  cakeculate = []
  for ingredient in recipe:
    if ingredient not in available:
      return 0
    else:
      cakeculate.append(int(available[ingredient] / recipe[ingredient]))
  return min(cakeculate)

# Test
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
