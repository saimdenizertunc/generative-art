# Non-overlapping Circles using Python and Processing

An experimental generative art work using Python and Processing

A random try:

![Demo1](https://i.imgur.com/dJvHe3P.gif)

Of course, we get different output every time we run it.

## Logic

Program iteratively repeats the same **basic** steps: setting random x and y coordinates on the canvas and a radius within certain limits. Then creates a circle.

**Rules**

- Created circle must not extend beyond the invisible circle frame around the canvas. (To check this, used some analytical geometry)
- To get started, create 2 invisible circles to add a little "artistic" and "human touch"
- If it goes beyond the frame try again (By doing this we get a arbitrary frame from the circle inside the canvas.)
- Each circle must be randomly[^1] positioned circles that do not overlap (To do this, I tested that the sum of the radii of each newly created circle with each other circle is greater than the distance between their centers)

### Colors

The most difficult concept with randomness is finding the right colors. Completely random RGB colors produce highly unaesthetic results.

Better results can be produced with a suitable color palette.

### To-Do

- [ ] Color selection correlated with the coordinates and radii of the created circles
- [ ] Making the position of the circular frame clear on the canvas
- [ ] Add more complexity

It was a project that I had a lot of fun. The limits of geometry, randomness and imagination are endless. :face_in_clouds:

[^1]: Among the randomly generated circles, those who follow the rules are selected. It's kind of controlled random.
