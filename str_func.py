def upper(x):
  """ функция принимает на вход строку и возвращает ее сооо всеми заглавными буквами!!!"""
  return ''.join([i for i in x if i.isupper()])

print (upper('ABcc'))

def upper_first(text):
  """функция делает заглавными первые буквы слов"""
  text = ' '.join(word[0].upper() + word[1:] for word in text.split())
  return text

print(upper_first('делаем первые буквы заглавными в python'))