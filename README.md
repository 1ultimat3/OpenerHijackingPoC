# Opener Hijacking PoC

##Intro

One of my favorite attacks, which were published recently, deals with hijacking the opener module. Since the attack has been [integrated into BeEF already](https://github.com/beefproject/beef/pull/1295), I have written a small PoC for presentation/teaching purposes.

More information on the opener hijacking attack can be found [here](https://www.jitbit.com/alexblog/256-targetblank---the-most-underestimated-vulnerability-ever/).

## Installation 
```
pip install -r requirements.txt
```

## Run
Start the local webserver first:

```
python opener_poc/views.py
```

Then open the browser and goto [http://localhost:5000/victim](http://localhost:5000/victim).

Afer clicking on the **Open PoC Link** a new window is opened, which contains the **Attacker Page**. At the same time, the opener page's location is also changed to **Phishing Page**. The **Phishing Page** contains the initial page in an iFrame (to demonstrate a possible chained clickjacking attack).