from bs4 import BeautifulSoup
from urllib.request import urlopen

print(
  """
  Enter: d and then after it the number of sides (e.g. d20) for that die, firstnumber-secondnumber to get a random number between firstnumber and second number (e.g. 5-10), or rollsdsides for that many rolls of a die with that many sides (e.g. 2d4)
  """
)

while True:
  to_roll = input("What would you like to roll? ")
  print("")
  url = f'https://dnddiceroller.zameerlovesmath.repl.co/{to_roll}'
  page = urlopen(url)
  html = page.read().decode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  print(soup.get_text())
  print("")