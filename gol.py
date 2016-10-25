#!/bin/python

class Board:
  aliveCells = set()

  def isCellAlive(self, x, y):
    return (x, y) in self.aliveCells

  def bringToLife(self, x, y):
    self.aliveCells.add((x, y))

  def evolve(self):
    cellsToDie = set()
    for cell in self.aliveCells:
      if self.countFriendsOf(cell) < 2:
        cellsToDie.add(cell)
    self.aliveCells -= cellsToDie

  def countFriendsOf(self, cell):
    friendsCount = 0
    x, y = cell
    for dx in range(-1, 2):
      for dy in range(-1, 2):
        neighbour = (x + dx, y + dy)
        if cell == neighbour:
          continue
        else:
          if neighbour in self.aliveCells:
            friendsCount += 1
    return friendsCount

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
 
def cellWithTwoFriendsSurvives():
  board = Board()
  board.bringToLife(0, 0)
  board.bringToLife(1, 1)
  board.bringToLife(2, 2)
  board.evolve()
  assert board.isCellAlive(1, 1) 

createdBoardHasDeadCell()
canBringOneCellToLife()
singleCellDiesOfLonelyness()
cellWithTwoFriendsSurvives()
