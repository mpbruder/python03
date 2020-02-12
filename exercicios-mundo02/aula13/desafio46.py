import emoji
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\n\n' + emoji.emojize(':fireworks:', use_aliases=True)
      + '  HAPPY NEW YEAR! 2020  '
      + emoji.emojize(':fireworks:', use_aliases=True))
