Here is our fully hosted [website](https://benholmgren.github.io/MTRuralHealth/)!

## Instructions for contribution
This site is run through jekyll, a hosting tool github uses. To locally host this site, you'll need to
install it. To do so, see these [instructions](https://jekyllrb.com/docs/installation/).
Jekyll makes hosting stuff pretty nice. For a tutorial on jekyll, maybe consider checking out the giraffe academy
jekyll tutorials on youtube, they're pretty helpful. All you'll need to do for practical purposes with jekyll here
is to potentially host locally on your machine. (on mac, use 'bundle exec jekyll serve')
If you're feeling good about a change, commit it and push it to the gh-pages branch ('git push origin gh-pages').
Github automatically hosts the site off of this branch, which is sweet.
When making changes, I'm expecting that we'll only really need to edit in the 'about' and 'destinations' sections of the site.
To do this, all you need to do is add a markdown file of the page you want to add, and it'll be available in the menu section of the
respective page if you simply designate the page in its respective .yml file. To add a page to the destination page, add this 'example.md'
in the _destination folder with the header:
```
---
title: Destinations
permalink: /destinations/example/
redirect_from: /destinations/example.html
---
```

Then change data/destination.yml to be:
```
- title: Destinations
  destinations:
  - home
  - example
```
Then push your changes and github should have the updated site hosted in 5 minutes or so. Often it only takes a matter of seconds, but sometimes
changes can take longer to update (~15 min maybe).
After this is all done, you should've added a new page to either the destinations or about sections, and you should see it on the website.
There is kinda a lot going on here, so if other changes are wanted and you're unsure of how to go about them, feel free to ask me about it.

To add scenes, I've just been adding links our course server, where I've downloaded videos of cool nature scenes.
Here's the code I've been using for the html pages which I've just put on my page on the course server (feel free to do this with yours as well)

```
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial;
  font-size: 17px;
}

#myVideo {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
}

.content {
  position: fixed;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  color: #f1f1f1;
  width: 100%;
  padding: 20px;
}

#myBtn {
  width: 200px;
  font-size: 18px;
  padding: 10px;
  border: none;
  background: #000;
  color: #fff;
  cursor: pointer;
}

#myBtn:hover {
  background: #ddd;
  color: black;
}
</style>
</head>
<body>

<video autoplay muted loop id="myVideo">
  <source src="fjord.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

<div class="content">
  <h1>Heading</h1>
  <p>Lorem ipsum dolor sit amet, an his etiam torquatos. Tollit soleat phaedrum te duo, eum cu recteque expetendis neglegentur. Cu mentitum maiestatis persequeris pro, pri ponderum tractatos ei. Id qui nemore latine molestiae, ad mutat oblique delicatissimi pro.</p>
  <button id="myBtn" onclick="myFunction()">Pause</button>
</div>

<script>
var video = document.getElementById("myVideo");
var btn = document.getElementById("myBtn");

function myFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "Pause";
  } else {
    video.pause();
    btn.innerHTML = "Play";
  }
}
</script>

</body>
</html>
```

I just found this on geeks for geeks, but it's been working great. Try it
out for yourself, changing fjord.mp4 to whatever video you'd like to upload, making sure to host this video on the course website.
(If we just host these videos on the github, we get git errors because I've already tried too many times to use large files on github and
they're mad at me.)
