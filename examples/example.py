import sys

from utils import pgn_to_gif, read_pgn

pgn = read_pgn(sys.argv[1])
pgn_to_gif(pgn=pgn, gif_path='./example.gif', duration=1.0)
