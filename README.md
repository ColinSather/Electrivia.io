# Orwell's Trivia
A trivia game that shocks players on wrong answers. Pretty dystopian right? [cringes]

Triva API Data: https://opentdb.com/api_config.php
JSON Formatter: https://jsonformatter.curiousconcept.com/#

## Notes to self
3/31/2021
I've decided to do everything server side. I'm sure there are some benefits for client side rendering, in fact I like the idea of handling all the JSON logic all on the front end and having the backend simply do iOT stuff. However I think implementing a front end javascript framework such as React js would be overkill. 

The only reason I am using python in the first place is because it controlls GPIO pins VERY quickly, with little lag.

3/27/2021
I am not sure what I want to do for the front end yet. Which is why all the flask routes simply return strings
containing html data. The "database" consists of a single json file, again not sure what to do about that either.
The only reason I am using this framework is because python works really well with the raspberry pi and iOT devices in general.
