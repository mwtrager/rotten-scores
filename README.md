# Work in Progress

## but if you would like to try it:

You will need:
..[Python 3](https://www.python.org/downloads/ "Python,org Download Page")
..[pip](https://pip.pypa.io/en/stable/installing/ "pip Installation Instructions") (it's likely you already have it installed, check with `pip -v` in your terminal)
..[Pipenv](https://packaging.python.org/new-tutorials/installing-and-using-packages/  "Pipenv Installation Instructions")

Then you can
`git clone https://github.com/mwtrager/rotten-scores.git`
`cd rotten-scores`
`pipenv --three`
'pipenv install'

To run:
'./main.sh <rottentomatoes.com movie link>'

All the output will be written into a file in a directory created at runtime: ./output/<movie name>

If the file doesn't exist it will create it and write to it.
If it does, it will append it.
