Sample run
==========

```
dmedvinsky at loki in ~/s/0/aarecog (master=)
><((°> ./aarecog.py samples/A
DEBUG recognizer.invariants.horizontal_solid: Got signature 1,2,1,2
DEBUG recognizer.invariants.vertical_solid: Got signature 1,2,1
INFO recognizer: Possible suggestions [{'A', 'S', 'R'}, {'P', 'D', 'A', 'Q', 'F', 'O'}]
A

dmedvinsky at loki in ~/s/0/aarecog (master %=)
><((°> ./aarecog.py samples/B
DEBUG recognizer.invariants.horizontal_solid: Got signature 1,2,1,2,1
DEBUG recognizer.invariants.vertical_solid: Got signature 1,3,1,2
INFO recognizer: Possible suggestions [{'C', 'B', 'G'}, {'B'}]
B

dmedvinsky at loki in ~/s/0/aarecog (master %=)
><((°> ./aarecog.py samples/B 2>/dev/null
B
```
