import game_of_life as gol

universe = gol.create_universe(100, 100)
universe = gol.init_structure([50, 50], gol.engine, universe)

gol.animate_universe(universe, generations=300)
