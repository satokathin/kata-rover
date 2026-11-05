import sys

class Rover:
    """
    Represent a rover moving across a plateau.

    Attributes:
        x (int): The x-coordinate of the rover's position.
        y (int): The y-coordinate of the rover's position.
        direction (str): The direction the rover is facing ('N', 'E', 'S', or 'W').
        plateau (Plateau): The plateau on which the rover is located.
    """

    DIRECTIONS = ['N', 'W', 'S', 'E']

    def __init__(self, x, y, direction, plateau):
        self.x = x
        self.y = y
        self.direction = direction
        self.plateau = plateau

    def turn_left(self):
        """Rotate the rover 90 degrees to the left."""
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index + 1) % 4]

    def turn_right(self):
        """Rotate the rover 90 degrees to the right."""
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index - 1) % 4]

    def move(self):
        """Move one position forward if the rover stays within the plateau."""
        if self.direction == 'N' and self.y < self.plateau.Ymax:
            self.y += 1
        elif self.direction == 'E' and self.x < self.plateau.Xmax:
            self.x += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1

    def action(self, commands):
        """Execute movement commands and return the rover's final state.

        Args:
            commands (str): A sequence of 'L' (left), 'R' (right), and
                'M' (move) commands. Other characters are ignored.

        Returns:
            str: The final x-coordinate, y-coordinate, and heading,
                separated by spaces.
        """
        actions = {"L" : self.turn_left, "R" : self.turn_right, "M": self.move}
        for command in commands:
            if command in actions:
                actions[command]()
        return f"{self.x} {self.y} {self.direction}"

class Plateau:
    """Represent a rectangular plateau with maximum x and y coordinates.

    Attributes:
        Xmax (int): The maximum x-coordinate.
        Ymax (int): The maximum y-coordinate.
    """

    def __init__(self, Xmax, Ymax):
        self.Xmax = Xmax
        self.Ymax = Ymax

def main ():
    """Read rover instructions from a file and print each rover's final state.

    The input file path is provided as the first command-line argument. The
    file contains plateau dimensions followed by position and command lines
    for each rover.
    """
    file = sys.argv[1]
    with open(file, 'r') as f:
        lines = [l.strip() for l in f if l.strip()]

    plateau_line = lines[0].split()
    xMax = int(plateau_line[0])
    yMax = int(plateau_line[1])
    plateau = Plateau(xMax, yMax)

    for i in range(1,len(lines), 2):
        rovers_positions = lines[i].split()
        x = int(rovers_positions[0])
        y = int(rovers_positions[1])
        direction = rovers_positions[2]

        rovers_commands = lines[i+1]
        rover = Rover(x, y, direction, plateau)
        print(rover.action(rovers_commands))

if __name__ == "__main__":
    main()