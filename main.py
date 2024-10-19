import os

from controller.controller import Controller, set_paths
from model import Paths


def main():
    set_paths(os.getcwd())
    Controller().start()


if __name__ == '__main__':
    main()

