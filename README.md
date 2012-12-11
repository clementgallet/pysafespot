## Introduction ##

Here is a python script to detect safe-spots in shmup patterns. The input is movie presenting the pattern and one of more bullet images (and masks). The algorithm aims at finding spots that are not crossed by bullets. We will see if it'a good idea...

## Requirements ##

- python version > x.x
- numpy (for dealing with arrays)
- opencv (for fast normalized cross-correlation. Might try something else)
