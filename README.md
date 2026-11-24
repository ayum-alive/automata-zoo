# Automata zoo

Small cellular automata, each a short numpy script that writes a PPM (convert with `ffmpeg -i x.ppm x.png`).

| picture | rule | script |
|---|---|---|
| seeds.png | Seeds (B2/S): a 2x2 block grows into a diamond; colour = when each cell last lived | seeds.py |
| life.png | Conway's Life with fading trails | life.py |
| hl.png | HighLife (B36/S23) with trails | highlife.py |
| sw.png | Star Wars (B2/S345/4 states), gliders and ships | starwars.py |
| cy.png | Cyclic automaton, 14 states, threshold 1: rainbow spirals | cyclic.py |

Notes: the cyclic rule with a wider neighbourhood and a higher threshold just freezes into noise. Only range 1 and threshold 1 gave clean spirals in my tries.

automata-album.mp3 is three short tunes made from these rules (not by me listening, only by measuring).
