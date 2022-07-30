<h1>SOLVING PUZZLE BY SEARCHING</h1>

## Implementing the Puzzle

The puzzle was implemented using the numpy library for the game logic and the pygame library for the interface. The game has three screens explained below:

![Home Screen](https://github.com/filipemedeiross/solving_puzzle_by_searching/blob/main/examples/home_screen.jpeg?raw=true)

The initial screen displays the puzzle dynamically from random movements and the **Play** button which, when clicked, starts the game with the current state of the pieces in the demo. It also has an **i** button that takes you to the game's github repository.

![Game Screen](https://github.com/filipemedeiross/solving_puzzle_by_searching/blob/main/examples/game_screen.jpeg?raw=true)

When the game starts, it displays the time count and the movements performed, while allowing the user to return to the home screen, perform the movements of interaction with the game and request the automatic resolution through the AI.

![Winner Screen](https://github.com/filipemedeiross/solving_puzzle_by_searching/blob/main/examples/winner_screen.jpeg?raw=true)

When you win the game, the time and moves are paused and the puzzle interaction and automatic solving functions are disabled. The function of returning to the home screen remains and the option to restart the game appears.

## Search Strategies

The tests folder contains the notebooks where the search algorithm tests were performed. The breadth-first search and backtracking depth-first search algorithms were tested. The first proved to be efficient for resolving instances with up to 12 steps and the second with up to 14 steps.

Considering that solving the puzzle requires an average of 22 steps, it was necessary to implement the A* search algorithm, which proved to be more efficient. Among the implementation options tested, the tree search was more efficient than the graph search, being the puzzle solving strategy adopted in the game.

## Puzzle Pack Organization
```
puzzle/                         Top-level package
      __init__.py
      constants.py
      logic_game.py
      puzzle.py                 It brings together the functionalities of the modules to implement the puzzle
      media/                    Folder with the .png files used in the game's interface
              ...
      formulations/             Can be extended with different puzzle settings
              __init__.py
              standard_form.py  Sets the default formulation of the puzzle problem
      search_algorithm/         Implementation of the A* tree search algorithm         
              __init__.py
              node.py
              priority_queue.py Sets the priority queue
```
## Running the Game

Using some Linux distro and make sure you have [Python 3](https://www.python.org/) installed.

Clone the project:

```bash
  git clone https://github.com/filipemedeiross/solving_puzzle_by_searching.git
```

Access the project directory:

```bash
  cd solving_puzzle_by_searching
```

Creating a virtual environment (for the example we use the location directory parameter as `.venv`):

```bash
  python3 -m venv .venv
```

Activating the virtual environment:

```bash
  source .venv/bin/activate
```

Install all required packages specified in requirements.txt:

```bash
  pip install -r requirements.txt
```

Use the following command to run the game:

```bash
  python3 -m puzzle.puzzle
```
## References

Norvig, Peter. Inteligência Artificial. Grupo GEN, 2013.

Images used: <https://opengameart.org/>

Numpy: <https://numpy.org/doc/stable/>

Pygame: <https://www.pygame.org/docs/>
