# Electrivia
A trivia game that electrocutes people...

Triva API data courtesy of Open Triva DB: https://opentdb.com/api_config.php

## MVP TODOs
* find a better way to hold down tens unit button

## Future TODOs
* use web sockets to enable each end user to view the same question
* allow users to create their own quizzes
* allow users to select a specific quiz instead of starting a random quiz
* package the hardware in a 3d printed box type thing
* some how make it easier to connect the device to WiFi
* Encorperate the LCD hardware
* Improve the styling of the app

## Bugs
* User gets shocked if the page is refreshed on an incorrect answer results page

## Notes to self
6/20/2021
I am considering re-writting this project as a Java Spring application. Using Java will make this project slightly faster which is necessary considering it's running on a raspberry pi. In addition, the Java re-write will be a good learning opportunity.

4/16/2021
To set up local dev server in centos use the below commands.

```
sudo firewall-cmd --runtime-to-permanent
sudo firewall-cmd --zone=public --add-port=5000/tcp
```

3/31/2021
I've decided to do everything server side. I'm sure there are some benefits for client side rendering, in fact I like the idea of handling all the JSON logic all on the front end and having the backend simply do iOT stuff. However I think implementing a front end javascript framework such as React js would be overkill. 

The only reason I am using python in the first place is because it controlls GPIO pins quickly, with very little lag.







