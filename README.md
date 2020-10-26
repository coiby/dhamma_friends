# Dhamma Friends

1. A basic portal to look up info on retreats and teachers

2. Self-organizing retreat

    Most retreats are held by an organization, i.e., by a retreat center. But someone may want to lead a retreat, someone may simply want to be a practitioner and others may volunteer to do the cooking, housing, etc. Can we pair up these people to make a successful retreat? (Personally I'm not sure this feature is needed. Firstly it seems meditation teachers are in high demand so I doubt how many users will actually regiter to lead a retreat. Secondly, considering there is a bit of risk doing a meditation retreat, a.k.a something like dark night, how can we make sure a teacher is qualitifed to handle this situation?

3. After creating a non-profit organization, there will be new features to be implemented like accepting donations online.

## How to setup the website locally

1. Install python-flask, take Arch-based distributions as an example,
```bash
# for the web service
pacman -S python-flask
```
2. Start the server
```bash
$ python hello.py
 * Serving Flask app "hello" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
3. Visit http://127.0.0.1:5000/ in the browser

## TODOs

 - [ ] User registration, logging in/out

### Retreat centers

 - [ ] Convert all retreat center info from [Wiki - www.dharmaoverground.org](https://www.dharmaoverground.org/dharma-wiki/-/wiki/Main/FrontPage#section-FrontPage-Retreat+Centers+and+Places+to+Practice) into sqlite format dhamma.db3
 - [ ] Comments or reviews on a retreat center
 - [ ] Search by location, tradition etc.
