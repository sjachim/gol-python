#!/bin/python

class Board:
  somethingIsAlive = False

  def isCellAlive(self, x, y):
    return self.somethingIsAlive

  def bringToLife(self, x, y):
    self.somethingIsAlive = True

  def evolve(self):
    self.somethingIsAlive = False

def createdBoardHasDeadCell():
  board = Board()
  assert not board.isCellAlive(0, 0)
  
def canBringOneCellToLife():
  board = Board()
  board.bringToLife(0, 0)
  assert board.isCellAlive(0, 0)
  
def singleCellDiesOfLonelyness():
  board = Board()
  board.bringToLife(0, 0)
  board.evolve()
  assert not board.isCellAlive(0, 0)
  

createdBoardHasDeadCell()
canBringOneCellToLife()
singleCellDiesOfLonelyness()
