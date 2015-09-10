# Stepwise

A super-simple Sublime Text 2 plugin to keep checkpoints of a file. Think of it as version control for babies. I use it to create step-by-step walkthroughs of my coding process/tutorials for my students.

Files are named `basename-step01.ext`, `basename-step02.ext`, etc.
## Use

`Command + Shift + P`, select `Stepwise: Activate for this file`. Then you'll be able to double-tap save to create a new version (two saves within 500ms).

You can also use `Stepwise: Create New Step` or `Tools > Stepwise: Save step` from the top menu. They'll both automatically activate Stepwise for the file and add a new version.

## Installation

### OS X

1. Open up Finder
2. Command+Shift+G
3. Type in `~/Library/Application Support/Sublime Text 2/Packages/`
4. Copy the `track_url` (or whatever it's called) directory into that folder
5. Open up Sublime Text 2 and rejoice

Or, if you're fancy, just clone the repo into that folder.

### Windows

Copy the folder to `%appdata%\Sublime Text 2` and you'll be good to go

