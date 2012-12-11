## Introduction ##

Here is a python script to detect safe-spots in shmup patterns. The input is movie presenting the pattern and one of more bullet images (and masks). The algorithm aims at finding spots that are not crossed by bullets. We will see if it's a good idea...

## Requirements ##

- python version > x.x
- numpy (for dealing with arrays)
- opencv (for fast normalized cross-correlation. Might try something else)

## My thoughts ##

Normalized cross-correlation (NCC) is a classic way of getting an index of how well a certain template match a portion of an image. It takes values between 0 and 1. Simple cross-correlation can be done quickly in the frequency-domain, but not the NCC. OpenCV has a build-in function to do that (check how fast it is ?), so we can use it. Converting from PIL images to numpy array then to OpenCV structure (and back) is easily done.

First problem: I have colored images, and NCC is done on numbers. I could use:
- luminosity
- magnitude following the RGB vector of the main color of the bullet
- on the internet, people use edge detection before matching, not very good for bullets I guess...

Second problem: Deal with the bullet mask. Maybe just set the background to the average luminosity/magnitude/whatever of the template. I need to check that mathematically.

Now, things are getting more complicate, as some bullets are behind others. We could use an iterative search, and "removing" pixels of already found bullets to allow partial match of bullets behind to become full match, like a mask, of an inverse mask, or whatever.

Wow, don't forget that we are dealing with animated pictures ! If a bullet has a straight trajectory, we could use that to strenghten the matching ! First idea: compute the NCC on each image, then if you put one image "on top of" the previous one, it becomes a 3D image, where bullet's trajectories are just 3D segments ! Now we can use a segment detector on that. Classic !

## Links ##

Sources that will help me:
- http://stackoverflow.com/questions/6991471/computing-cross-correlation-function

