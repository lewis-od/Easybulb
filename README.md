# Easybulb    
Python API for controlling Easybulb lights. Also works with MiLight and LimitlessLED bulbs.

## Usage    
```python
lights = Easybulb("ip address")
lights.off() # Turn the lights off
lights.on() # Turn the lights on
lights.colour(150) # Change the colour of the lights (values from 0-255)
lights.brightness(15) # Change the brightness of the lights (values from 1-59)
lights.disco() # Activate disco mode
lights.disco_faster() # Speed up disco mode
lights.disco_slower() # Slow down disco mode
```
