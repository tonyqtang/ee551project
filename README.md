EE551project_Tetris

=======

Rules:  
Different shaped blocks fall from the top of the screen, the player can adjust blocks' direction and position. when the block fall to the bottom or it touches another exist blocks, it lands and stops. Everytime player complete a row with no gaps in it, the row disappears and all rows above it move down and player scores 1 point. The player keeps gaining points until the exists blocks touch the top of the screen.

How to control:  
Use ← → to control position, ↑ to change direction, ↓ to accelerate falling speed, spacebar to fall to the end immediatly. use P to pause. 

Shapes of blocks:  
There will be seven shapes in this game and each shape forms by four squares.

![image](https://github.com/tonyqtang/ee551project/blob/master/different%20_blocks.jpg)

Player can change each shape's direction which means 90 degrees clock-wise each time when pressing ↑.

General steps in coding this game:  
1.Define the shape of blocks and what do they look like when diretion changed.  
2.Define the control command.  
3.Generate a random block.  
4.Judge if a block is landed.  
5.Erase a row if it is complete.  
6.Judge if blocks touch the top.

P.S. There is a game I really like in my phone called "1010!". It's similar to Tetris with different types of blocks. But you need to drag the block to its position instead of watching it falling down and it will erase all complete rows and columns. I'd like to try it when I learn how to write the classic one.

