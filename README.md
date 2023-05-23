# Minesweeper Game
This is a classic implementation of the Minesweeper game using the Pygame library. Minesweeper is a single-player puzzle game where the objective is to clear a rectangular board containing hidden mines without detonating any of them. The game is won by uncovering all the cells that do not contain mines but in my version the game is won by flagging all mines.

## How to Play
1. __Set Up a Virtual Environment:__ Open a terminal or command prompt and navigate to the directory where you want to create the virtual environment. Run the following command to create a new virtual environment named "venv":
    ```
    python -m venv venv
    ```
    
2. __Activate the Virtual Environment:__ Depending on your operating system, activate the virtual environment using one of the following commands:
    * For Windows:
        ```
        venv\Scripts\activate
        ```
    * For macOS/Linux:
        ```
        source venv/bin/activate
        ```

3. __Install Dependencies:__ Once the virtual environment is activated, you need to install the required dependencies. Run the following command to install Pygame:
    ```
    pip install -r requirements.txt
    ```

4. __Launch the Game:__ After installing the dependencies, navigate to the directory where the game files are located. Make sure your virtual environment is still active. Run the following command to start the game:
    ```
    python main.py
    ```
    
5. __Game Controls:__ The game can be controlled using the following keys:  
    * Left Click: Uncover a cell.
    * Right Click: Flag or unflag a cell to mark it as a potential mine location.
    * Esc: Restart the game.
    * Game has three difficulty levels you can choose: 
        1. __Easy:__ 10x10 minefield with 10 mines
        2. __Medium:__ 20x20 minefield with 45 mines
        3. __Hard:__ 30x30 minefield with 120 mines

6. __Game Rules:__ The rules are simple:
    * Each cell on the board can be in one of three states: covered, uncovered, or flagged.
    * Uncover a cell by left-clicking on it. If the cell contains a mine, the game is over.
    * If a cell does not contain a mine, it will display a number indicating the number of neighboring cells that contain mines.
    * Use these numbers as hints to determine the location of mines.
    * Flag a cell by right-clicking on it to mark it as a potential mine location. Right-clicking on a flagged cell will unflag it.

7. __Game Over:__ The game ends in one of two ways:
    * If you uncover a cell containing a mine, you lose.
    * If you successfully flag all cells that do contain mines, you win.
        > **_NOTE:_**  it is my quirky way to win because I was in a hurry making this game and didn't think to google the correct rules

## Tecnical Details
The Minesweeper game is implemented using the Pygame library, which provides a set of tools for building games in Python. The game logic and graphical user interface (GUI) elements are separated into different classes to keep the code organized and maintainable.

The game board is represented by a 2D grid, and each cell on the grid is an instance of the `Cell` class. The `Minefield` class handles the minefield logic, including mine placement, cell uncovering, and win/lose conditions.

All game windows and states are instances of a `State` class, which handles state initializaiton, transitions between stages, event handling and rendering. States in their own order are registered and controlled by an instance of a `StateManager`, which is used to register and switch between screens (start, game, win/loss).

The GUI and graphics elements, such as buttons, cells, mines are implemented using images. All the text is just a plain text created and rendered using Pygame.

## Contribution
Contributions to this version of Minesweeper game are welcome. If you have any ideas, bug fixes, or improvements, feel free to submit a pull request or open an issue on the project's GitHub repository. All the things I wanted to add are written inside `todo.md` file.

## License
This Minesweeper game is released under the Apache 2.0 License. Feel free to use, modify, and distribute the code as per the terms of the license.
