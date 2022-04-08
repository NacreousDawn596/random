# random
a little code to generate random number without using any external lib


# generate a random number
```py
import generate
print(generate.number(0, 10))
```
or
```py
from generate import number
print(number(0, 10))
```


# generate a random element from an array
```py
import generate
liste = [0, 1, 2, 3, 4, 5, "blue pen", "black pen", True, False]
print(generate.from_list(liste))
```
or
```py
from generate import from_list
liste = [0, 1, 2, 3, 4, 5, "blue pen", "black pen", True, False]
print(from_list(liste))
```

# shuffle an array
```py
import generate
liste = [0, 1, 2, 3, 4, 5, "blue pen", "black pen", True, False]
print(generate.rearrange(liste))
```
or
```py
from generate import rearrange
liste = [0, 1, 2, 3, 4, 5, "blue pen", "black pen", True, False]
print(rearrange(liste))
```

**Enjoy!**
