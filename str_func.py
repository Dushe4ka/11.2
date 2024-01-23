def upper(x):
  """ функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами."""
  return ''.join([i for i in x if i.isupper()])

print (upper('ABcc'))
