# Codewars: Text Align Justify
# Source: https://www.codewars.com/kata/537e18b6147aa838f600001b/train/python

def justify(text, width):
  endofline = width-1
  answer = ''
  while endofline < len(text):
    barrier = 0 if endofline-width < 0 else endofline - width
    if endofline == len(text) - 1:
      break
    if text[endofline] != ' ' and text[endofline+1] == ' ':
      endofline += 1
    else:
      while text[endofline] != ' ' and endofline != barrier:
        endofline -= 1
      if endofline == barrier: 
        endofline += width
    extractText = text[barrier:endofline]
    charCount = len([1 for x in extractText if x != ' '])
    availableSpace = width - charCount
    words = list(filter(lambda x: x != '', extractText.split(' ')))
    spaces = len(words) - 1
    if spaces == 0:
      finalText = words[0]
    else:
      additionalSpace = availableSpace % spaces
      spaceLength = int(availableSpace/spaces)
      finalText = ''
      for word in range(len(words)):
        finalText += words[word]
        if word < len(words) - 1:
          finalText += ' ' * spaceLength
          if additionalSpace > 0:
            finalText += ' '
            additionalSpace -= 1
    answer += finalText + '\n'
    endofline += width
  lastText = text[endofline-width:]
  words = list(filter(lambda x: x != '', lastText.split(' ')))
  finalRowText = ''
  for word in range(len(words)):
    finalRowText += words[word]
    if word < len(words) - 1:
      finalRowText += ' '
  answer += finalRowText
  return answer

print(justify('123 45 6', 7))
print(justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.', 15))

# Alternate Better Solution
def justify2(text, width):
    lines, last = [[]], -1
    for word in text.split():
        if last + 1 + len(word) > width:
            lines.append([word])
            last = len(word)
        else:
            lines[-1].append(word)
            last += len(word) + 1

    def justify_line(words):
        if len(words) == 1:
            return words[0]
        interval, extra = divmod(width - sum(map(len, words)), len(words) - 1)
        init = (word + ' ' * (interval + (i < extra)) for i, word in enumerate(words[:-1]))
        return ''.join(init) + words[-1]

    return '\n'.join(map(justify_line, lines[:-1]) + [' '.join(lines[-1])])
