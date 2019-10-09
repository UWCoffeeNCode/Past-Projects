# Archery

## Controls:
- move your cursor to aim the bow and left-click to place the bow
- move your cursor to aim the arrow and control its speed and left-click to fire the arrow
- left-click to retrieve your arrow and repeat the above two-steps to continue playing

## Features:
- [x] projectile motion 
- [x] sprite and tile-graphics for bow, arrow, crosshair, board, background, and grass
- [x] arrow-target and arrow-ground collisions
- [x] vertically moving board
- [x] mouse control scheme
- [x] pivoting the bow based on the location of the crosshair
- [x] rotating the arrow based on its velocity in flight
- [x] having the arrow get stuck in the target at whatever orientation it was in prior to hitting the target
- [x] random grass generation

##### Features to Implement:
- [ ] ammo system for arrow count
- [ ] score system based on location of arrow-board impact
- [ ] more complex board movement patterns
- [ ] increasing difficulty for every target that is successfully hit before arrows run out
- [ ] different level backgrounds

##### Known Bugs List:
- if an arrow hits the very bottom of the target and the target hits the ground, the arrow will stick to the ground
- framerate can drop sharply for unknown reasons
- the bow should not be able to be fired while it's under the ground
- at very high speeds, the arrow and board do not always collide
