# RXKBot - The only Discord bot you need.

Bot that randomly quotes RXKNephew lyrics.

Included songs are left as a comment in the lyrics file.

### Requires the discord.py and dotenv modules.
```
$ pip3 install discord.py dotenv [--break-system-packages(if pip complains about breaking packages)]

(or, if pip doesn't allow you to install dotenv)

$ sudo apt install python3-dotenv [adjust for package manager]
```

Don't forget to edit the ```.env``` file and add your own token. The bot will not run if you don't adjust it.

```
$ python main.py
```
