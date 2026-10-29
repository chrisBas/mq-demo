# workspace

Dagboards, and the Logic Bricks they run, from the [dagboard.ai](https://dagboard.ai) app.

[Open in Dagboard.ai](https://dagboard.ai/open?src=git:github.com/chrisBas/mq-demo) opens this repo's dagboards in the app, from its default branch. Opening them runs this repo's Python code in your browser, once you've reviewed it: the app shows you the code first, and runs none of it until you trust it.

## What's here

- `pyproject.toml`: the library, `workspace`, by name under `[tool.bricks]`.
- `workspace/`: the library's own Logic Bricks, each a Python module with a `handle()` function.
- [`dagboards/`](dagboards/): each dagboard, as a `.dgb` file of readable JSON, which names its bricks `<library>/<module.path>`, such as `workspace/double`.
- `data/`: the files the bricks read.
- `.dagboard/`: the app's own files: the settings, the lock with the libraries' versions and runtimes, each brick's metadata, and the dagboards' last results, which git ignores unless a dagboard keeps them in `dagboards/`.

The app writes this file when the folder has none, and leaves it to you once you change it.
