# Game Of Life
The Game of Life implementation in Python3. Just for Fun!

## Before you run
It uses numpy and matplotlib. For matplotlib animation to work under windows, you might have to have ffmpeg installed.

The following link may help you with that. https://www.wikihow.com/Install-FFmpeg-on-Windows

`run python test.py` to test the code. It will also generate mp4 file for the animation. If you dont want to,
then you can disable it in `animate_universe()` function.

Example:

```python
import game_of_life as gol

universe = gol.create_universe(100, 100)
universe = gol.init_structure([50, 50], gol.engine, universe)

gol.animate_universe(universe, generations=300)
```