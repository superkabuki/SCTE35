# Make an executable with Cython and threefive

* _One important note, using cython to compile threefive actually makes threefive run considerably slower but you may want an executable for other reasons_  

* Lets do a speed test  on a __4.7 GB__ video with __513 SCTE35 cues__


| Test             | seconds     |    
|------------------|----------   |
| python3.11       |     __11.81__   |
|                  |             |
| __pypy3.9__          |     __4.13__    |
|                  |             |
| cython compiled  |     __15.62__   |


pypy3 wins by a mile, but even python3.11 beats cython.


## You can make your threefive script an executable with cython.  
1. pip install cython `python3 -mpip intall cython`
2. I'm going to use the threefive cli tool for this example, it's probably installed as `~/.local/bin/threefive` or `/usr/local/bin/threefive`.
3. copy the threefive cli tool to your current directory and name it `threefive.pyx`
4. run `cython --embed threefive.pyx -o threefive.c`
5. compile with `clang -Os -I /usr/include/python3.11 threefive.c -lpython3.11  -o threefive`
6. You can do this with your own scripts the same way.
