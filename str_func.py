def upper(x):
  """ функция принимает на вход строку и возвращает ее сооо всеми большими буквами!!!"""
  return ''.join([i for i in x if i.isupper()])

print (upper('ABcc'))