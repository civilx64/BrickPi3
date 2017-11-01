# Initial software design notes
## Minimum Viable Application (MVA)
- Static-mounted
- Fired via touch sensor only
- *not* automatic - each shot must be triggered individually

## Requirements gathering
- *Blaster* has a *trigger* and a firing *pin*.
- A *push* of the *trigger* causes the *pin* to *fire*.
- *Blaster* has a *safety* mechanism that must be in the *OFF* position, or the *pin* will not *fire*.

## Initial Class Responsibility Collaborators (CRC)
- Blaster (inherits from BrickPi)
- Trigger (inherits from Sensor w/ enum 'NXT_TOUCH'
- Pin (inherits from Motor)

## Other Notes
- Blaster has a limited clip.
-- Pin will only fire a certain number of times before a reload is required.
-- Safety must be turned off to reload.
-- Safety must then be turned back ON to fire.
-- 15 >= 'CLIP_SIZE' >= 1
