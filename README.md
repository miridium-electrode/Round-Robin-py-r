# Round Robin to csv

a little adventure where i turn a round robin schedulling into csv file, the main component of this is:
1. contoh-static.py:
    the python script that take round robin related input and then display table
2. contoh1.py:
    the script that take round robin input and then give option for exporting to csv file

# the Pipfile
it has tabulate and pylint, you'll need it

# dependency
- R
    - rmarkdown
    - kableExtra
- texlive
- python3
    - Pygments
    - tabulate

# how to run
tested on linux(ubuntu 20.04), i don't know for windows or macs
1. download python3
2. download pip3
3. download Pygments, and add $HOME/.local/bin to path
    ```
    pip3 install --user Pygments
    echo "export PATH=$HOME/.local/bin >> ~/.bashrc && source ~/.bashrc
    ```
4. download pipenv
5. Pipenv install in cloned dir
6. python3 contoh-static.py
7. render .rmd file 
