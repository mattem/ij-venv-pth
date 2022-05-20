# IJ IDEA .pth files in venv

1. Create a Python venv in the root of the workspace: 
   1. `python3 -m venv .venv`
2. Add a `.pth` file to the `site-packages` folder of the created venv, add a relative path to the `libs` folder to it:
   1. `echo "../../../../libs" > .venv/lib/python3.9/site-packages/libs.pth`
3. Add the venv as an SDK to IJ
4. Note now in `__main__.py`, IJ is unable to resolve the import of `logger`

## Testing outside of IJ
1. Activate the venv `. .venv/bin/activate`
2. Run the `__main__.py` file: `python3 __main__.py`
3. Note how this correctly imports and prints message, as the `.pth` file is processed.

eg:
```
$ python3 __main__.py
[IJ] hello
```