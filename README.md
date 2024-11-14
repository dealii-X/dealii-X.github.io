## Installation instructions for mkdocs

    pip install mkdocs
    pip install mkdocs-material
    pip install markdown-include

Alternatively you can use conda to install all packages into a new environment named `dealii-website` like this:

    conda env create -f environment.yml

Then the server can be run locally as

    mkdocs serve

and you should see something like

    INFO    -  Documentation built in 0.15 seconds
    INFO    -  [08:40:55] Watching paths for changes: 'docs', 'mkdocs.yml'
    INFO    -  [08:40:55] Serving on <http://127.0.0.1:8000/>
    INFO    -  [08:40:57] Browser connected: <http://127.0.0.1:8000/>

## Notes

 - Large asset files are stored in a separate git repository
   <https://github.com/dealii/website-large_assets>

   You can check out the repository as a git submodule:
   ```
   git submodule update --init
   ```

 - If you want to add to the timeline, access this google document, and ask for access write permission:
   <https://docs.google.com/spreadsheets/d/1FYT2_aIxZT4VFJeJDrqAu5out9HwCDwsxWU299e5hlk/edit?gid=0#gid=0>

   This is generated from this template:

   https://timeline.knightlab.com/#help
   https://timeline.knightlab.com/docs/using-spreadsheets.html#title_slides


