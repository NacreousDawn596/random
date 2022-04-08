import generate

### printing a random number
random_number = generate.number(0, 10)
print(random_number)

### printing a random element of an array
liste = [0, 1, 2, 3, 4, 5, "blue pen", "black pen", True, False]
element = generate.from_list(liste)
print(element)

### printing a shuffled array
liste = [0, 1, 2, 3, 4, 5, "blue pen", "black pen", True, False]
new_list = generate.rearrange(liste)
print(new_list)

########  ###  ##       ########    ####    ##   ##  ##
##        #### ##          ##     ##    ##   ## ##   ##
########  ## ####   ##     ##     ##    ##     ##    ##
##        ##  ###   ##     ##     ##    ##    ##
########  ##   ##   #########       ####     ##      ##
