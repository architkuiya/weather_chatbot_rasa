# Rasa weather chatbot

Rasa weather chatbot implemented during Xornadas Anita Borg 2022.


## viesure challenge

Prove your knowledge and add a new conversation to this weather chatbot.

- We are consuming the Open Weather API, and this is the JSON result:

<img width="319" alt="Screenshot 2022-05-04 at 13 49 23" src="https://user-images.githubusercontent.com/22213075/166675437-a9d279f7-9832-4d32-8355-6faf4e65aad7.png">

Right now, our Custom Action Server returns what is inside `main` and we pick the temperature (`temp`) and convert it to Celsius. This action is triggered when the user's intent is "ask for weather prediction". We can give the user a more precise response if:

- We only return the temperature when the user asks for the temperature (not the weather prediction).
- We can return the weather prediction itself (if it is sunny, there are clouds, it's raining... so what we get inside `weather`).
- We can return the maximum temperature, and/or the minimum.
- We can return the wind.
- And more options could be: a summary with the temperature, weather, wind, humidity, etc., the sunrise time, the sunset time...


How can you contribute? 

1. Please first check the pull requests and see if no one is working on your idea.
2. Create a PR with a clear title and description of your feature.
3. Start working on it! Whenever you have any queries, please feel free to contact me :)
4. When you are done, ping me in the PR and I will review it and merge it.
