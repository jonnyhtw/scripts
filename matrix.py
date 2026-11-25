#! /usr/bin/env python3

# Author: Joao S. O. Bueno
# gwidion@gmail.com
# GPL. v3.0

import math
import random
import shutil
import sys
import time

FRAME_DELAY = 0.075
CHARS = "0123456789" + "".join(chr(code) for code in range(0xFF66, 0xFF9E))
CSI = "\x1b["


class Stream:
    def __init__(self, rows):
        self.rows = rows
        self.head = random.uniform(-rows, rows)
        self.speed = random.uniform(0.35, 1.1)
        self.length = random.randint(max(2, rows // 3), max(3, rows))
        self.characters = [random.choice(CHARS) for _ in range(rows)]

    def advance(self):
        self.head += self.speed
        if self.head - self.length >= self.rows:
            self.head = random.uniform(-self.rows, -1)
            self.speed = random.uniform(0.35, 1.1)
            self.length = random.randint(max(2, self.rows // 3), max(3, self.rows))
        if random.random() < 0.2:
            self.characters[random.randrange(self.rows)] = random.choice(CHARS)

    def cell(self, row):
        distance = math.floor(self.head) - row
        if distance < 0 or distance >= self.length:
            return " ", 0
        if distance == 0:
            color = 15
        elif distance < self.length / 3:
            color = 46
        elif distance < self.length * 2 / 3:
            color = 34
        else:
            color = 22
        return self.characters[row], color


def draw_frame(streams, rows, cols):
    output = []
    color = None
    for row in range(rows):
        output.append(f"{CSI}{row + 1};1H")
        # Avoid writing the bottom-right cell, which can scroll the terminal.
        width = cols - 1 if row == rows - 1 else cols
        for stream in streams[:width]:
            char, cell_color = stream.cell(row)
            if cell_color != color:
                output.append(f"{CSI}38;5;{cell_color}m")
                color = cell_color
            output.append(char)
    sys.stdout.write("".join(output))
    sys.stdout.flush()


def main():
    size = None
    streams = []
    while True:
        cols, rows = shutil.get_terminal_size()
        if (cols, rows) != size:
            size = cols, rows
            streams = [Stream(rows) for _ in range(cols)]
            sys.stdout.write(f"{CSI}2J")
        for stream in streams:
            stream.advance()
        draw_frame(streams, rows, cols)
        time.sleep(FRAME_DELAY)


def doit():
    try:
        sys.stdout.write(f"{CSI}?1049h{CSI}?25l{CSI}40m{CSI}2J")
        sys.stdout.flush()
        main()
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(f"{CSI}0m{CSI}?25h{CSI}?1049l")
        sys.stdout.flush()


if __name__ == "__main__":
    doit()
