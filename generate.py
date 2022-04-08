def number(min, max):
  new_set = set()
  for i in range(min, max):
    new_set.add(str(i))
  for e in new_set:
    return int(e)

from_list(liste):
  new_set = set()
  for i in range(len(liste)):
    new_set.add(str(i))
  for e in new_set:
    return liste[int(e)]
      
rearrange(liste):
  new_list = []
  new_set = set()
  for i in range(len(liste)):
    new_set.add(str(i))
  for e in new_set:
    new_list.append(liste[int(e)])
  return new_list
