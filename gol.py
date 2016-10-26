#!/bin/python

class Board:
  def __init__(self):
    self.aliveCells = set()

  def isCellAlive(self, x, y):
    return (x, y) in self.aliveCells

  def bringToLife(self, x, y):
    self.aliveCells.add((x, y))

  def evolve(self):
    cellsToDie = set()
    newBornCells = set()
    for cell in self.aliveCells:
      if self.countFriendsOf(cell) not in {2, 3}:
        cellsToDie.add(cell)
    for cell in self.newBornCandidates():
      if self.countFriendsOf(cell) == 3:
        newBornCells.add(cell) 
    self.aliveCells |= newBornCells
    self.aliveCells -= cellsToDie

  def countFriendsOf(self, cell):
    friendsCount = 0
    for n in self.neighboursOf(cell):
      if n in self.aliveCells:
        friendsCount += 1
    return friendsCount

  def newBornCandidates(self):
    return {n for c in self.aliveCells for n in self.neighboursOf(c)}

  def neighboursOf(self, cell):
    x, y = cell
    for dx in range(-1, 2):
      for dy in range(-1, 2):
        neighbour = (x + dx, y + dy)
        if cell == neighbour:
          continue
        else:
          yield neighbour

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

def threeCellsGiveBirthToNewCell():
  board = Board()
  board.bringToLife(0, 0)
  board.bringToLife(2, 0)
  board.bringToLife(2, 2)
  board.evolve()
  assert board.isCellAlive(1, 1) 

def cellsDieOfOverpopulation():
  board = Board()
  board.bringToLife(0, 0)
  board.bringToLife(2, 0)
  board.bringToLife(1, 1)
  board.bringToLife(0, 2)
  board.bringToLife(2, 2)
  board.evolve()
  assert not board.isCellAlive(1, 1) 

createdBoardHasDeadCell()
canBringOneCellToLife()
singleCellDiesOfLonelyness()
cellWithTwoFriendsSurvives()
threeCellsGiveBirthToNewCell()
cellsDieOfOverpopulation()

print "Success. Tests passed."
