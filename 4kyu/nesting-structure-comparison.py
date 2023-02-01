# Codewars: Nesting Structure Comparison
# Source: https://www.codewars.com/kata/520446778469526ec0000001/train/python

def same_structure_as(original,other):
  if type(original) != list or type(other) != list:
    return False
  def create_template(input):
    template = []
    for e in input:
      if type(e) != list:
        template.append(0)
      else:
        template.append(create_template(e))
    return template
  return create_template(original) == create_template(other)

print(same_structure_as([1,2,3,4], [3,4,5,6]))