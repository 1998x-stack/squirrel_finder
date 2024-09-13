# Squirrel Finder

Squirrel Finder is a fun, retro-style game built using Python and Pygame. In this game, you control a koala that moves around the screen using the arrow keys. Your goal is to avoid bouncing strawberries and catch the squirrel to win the game.

## Table of Contents
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Flow](#game-flow)
- [Configuration](#configuration)
- [Logging](#logging)
- [Acknowledgements](#acknowledgements)

## Project Structure

The repository is structured as follows:

```
squirrel_finder/
│
├── main.py             # Main entry point of the game
├── player.py           # Player (Koala) logic
├── entity.py           # Generic entity class for enemies (strawberries, squirrel)
├── game.py             # Core game loop and logic
├── config.py           # Configuration and hyperparameters
├── logger.py           # Event logging for the game
├── assets/             # Game assets (images)
│   ├── koala.png
│   ├── strawberry.png
│   ├── squirrel.png
│   └── (other asset files)
└── sounds/             # Sound files for win and lose events
    ├── win_sound.wav
    └── lose_sound.wav
```

### Files Overview

- `main.py`: The entry point of the game where the game is initialized and started.
- `player.py`: Contains the `Player` class, which handles the movement and behavior of the koala.
- `entity.py`: Defines the `Entity` class, which is a generic class for objects that move around the screen, such as strawberries and the squirrel.
- `game.py`: Contains the main game loop and logic, including spawning enemies and checking for collisions.
- `config.py`: Centralized configuration file where you can adjust screen size, asset paths, sound paths, and other hyperparameters.
- `logger.py`: Provides basic logging functionality to track game events like player wins, losses, and resets.

## Requirements

Make sure you have the following dependencies installed before running the game:

- Python 3.6+
- Pygame

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/1998x-stack/squirrel_finder.git
   cd squirrel_finder
   ```

2. Install the required Python dependencies:
   ```bash
   pip install pygame
   ```

3. Ensure the necessary assets and sound files are in the correct directories:
   - `assets/` for image files (e.g., `koala.png`, `strawberry.png`, `squirrel.png`)
   - `sounds/` for sound files (e.g., `win_sound.wav`, `lose_sound.wav`)

## How to Play

1. Run the game by executing the following command:
   ```bash
   python main.py
   ```

2. Use the arrow keys to move the koala around the screen.
3. Avoid the bouncing strawberries.
4. Catch the squirrel to win the game.
5. The game will automatically restart if you win or lose.

### Game Controls

- **Arrow keys**: Move the koala.
- **Objective**: Avoid the strawberries and catch the squirrel.

## Game Flow

1. **Start Screen**: The game starts with an instruction screen. Press any key to start.
2. **Playing State**: The koala moves around the screen. Strawberries will spawn every second, and the squirrel will appear after 3 seconds.
3. **Win Condition**: If the koala touches the squirrel, you win the game, and the win sound plays.
4. **Lose Condition**: If the koala touches a strawberry, you lose the game, and the lose sound plays.
5. **Game Reset**: After a win or loss, the game automatically resets after a short delay.

## Configuration

You can customize various settings in the `config.py` file. The following parameters are available:

- **Screen settings**: `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`
- **Game limits**: `MAX_STRAWBERRIES`
- **Asset paths**: `KOALA_IMG_PATH`, `STRAWBERRY_IMG_PATH`, `SQUIRREL_IMG_PATH`
- **Sound paths**: `WIN_SOUND_PATH`, `LOSE_SOUND_PATH`
- **Font settings**: `FONT_SIZE`, `INSTRUCTION_FONT_SIZE`

Example:

```python
# config.py

# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Asset Paths
KOALA_IMG_PATH = 'assets/koala.png'
STRAWBERRY_IMG_PATH = 'assets/strawberry.png'
SQUIRREL_IMG_PATH = 'assets/squirrel.png'

# Sound Paths
WIN_SOUND_PATH = 'sounds/win_sound.wav'
LOSE_SOUND_PATH = 'sounds/lose_sound.wav'
```

## Logging

Game events such as player wins, losses, and resets are logged into the `game_log.txt` file. This is helpful for debugging or tracking game activity.

The following events are logged:
- Game start
- Player win
- Player loss
- Game reset

## Acknowledgements

- **Pygame**: [Pygame](https://www.pygame.org) was used for the game development.
- **Assets**: The images and sounds used in this project are placeholders. Feel free to replace them with your own.