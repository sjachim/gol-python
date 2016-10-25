#!/bin/python

class Board:
  def isCellAlive(self, x, y):
    pass 

def createdBoardHasDeadCell():
  board = Board()
  assert not board.isCellAlive(0, 0)
  

createdBoardHasDeadCell()
