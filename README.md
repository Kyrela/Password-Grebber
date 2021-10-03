<br>
<div style="text-align:center"><img alt="image" height="150" src="https://hosting.webspell.fr/images/2021/09/29/53db295f088f1d1cf51e2a111f7336c4.png" width="150"/>
<h1>Password Grebber</h1></div><br>


Password Grebber is a simple password generator software, based on a key relative to the context
(exemple : website name). You want to login/register to a website ? simply copy the website name in password grebber,
and it will give you your password. **No passwords, even encrypted, are ever saved**.

You will just have to write your generation script, Password Grebber will take care of the rest.

## Functionalities

 - Multiple password modes
 - Easy usage and configuration (python bases required)
 - GUI and auto versions

## Requirements

 - Python 3.6 or above
 - dependencies specified in [requirements.txt](requirements.txt) - for the auto version only

## Configuration

Open the [generator file](generator.py). Replace the tuple `modes` with the name of the different modes you want to set.
The first one is corresponding to 0, the seconde 1, etc...

Add in the `generate` function a generation method for each mode you configured, using `if` statements, just like in
the given exemple. You will have to use
[string manipulation](https://www.pythonforbeginners.com/basics/string-manipulation-in-python) in python for this.

## Build

If you want to build a binary file, once you configured your generation method,
use [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) or simply
[pyinstaller](https://pypi.org/project/pyinstaller/) with this command (for the GUI version) :

```bash
pyinstaller --noconfirm --onefile --windowed --icon "assets/logo.ico" --add-data "assets/info.png;assets" --add-data "assets/languages.json;assets" --add-data "assets/logo.png;assets"  "Password Grebber.pyw"
```

or this command (for AutoGrebber) :

```bash
pyinstaller --noconfirm --onefile --windowed --icon "assets/logo.ico" "AutoGrebber.pyw"
```

You can also replace `--onefile` with `--onedir` if you prefer having a whole directory instead of a single file.

## Usage

### GUI

Run the program, simply type or paste the key (generally the website name), change the generation mode if needed
and press enter or click on the `generate/copy` button. The generated password is copied and ready to paste !

![screenshot of the program](https://hosting.webspell.fr/images/2021/10/03/e95416f2a1c4f9379d48980d738f80e3.png)

*Pro tip: you don't have to paste the key or click on the paste button manually, because if the text field is empty,
your clipboard content will be automatically pasted!*

### Auto

This program is intended to be mapped as a keyboard shortcut or macro key, and only works with the first mode.
copy the key, launch the program, and the generated password will automatically be written!
(Note: It may not work on Linux)

## Contribute

If your native language isn't supported, just add the translated lines in [languages.json](assets/languages.json),
and be sure to send a pull request!

------------------------------------------------------------------------
Credits : [Kyrela](https://github.com/Kyrela)