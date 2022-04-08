def pig_latin(text):
  words = text.split()
  say = []

  for word in words:
    word = word[1:] + word[0] + 'ay'
    say.append(word)

  return ' '.join(say)

print(pig_latin("hello how are you"))