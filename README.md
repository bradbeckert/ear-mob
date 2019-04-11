# ear mob
ear mob music is the one and only place to find music reviews. all other reviewers are fuckin cucks. ya you heard me say it you little bitch what's your [REDACTED] and contact your mom to learn her bean pie recipe. that's really what this is all about just want some delicious bean pie. god what could be better than that. just slurpy sloshin all up and down my throat those delicious beans. how do people get beans to be so sweet and why don't we use beans as a sweetener in america it's messed up. maybe William Howard Taft wouldn't have been so fat if he ate less high fructose corn syrup and more of your bangin milf mom's bean pie. 

---

## Todo List - Script to Transfer from Google Sheets to Squarespace:
* Figure out Google Sheets API.
  * Connect to individual spreadsheets.
	* Parse data (e.g. artist, album, genre, year, & rating) properly for each Sheet.
* Figure out Squarespace API.
  * Connect to earmob.com.
  * Create blog posts.
  * Populate blog posts with spreadsheet information.
* Learn how to use `cron`.
  * Determine proper time interval.
* Use `requirements.txt` instead of keeping all the packages in the repo?
* Squarespace seems to be using its own git repo, this could be an issue?
	* Seems like it switches branches when you enter the `template` directory.
	
---

## Installation Instructions

1. Clone the repo.
2. Create a virtual environment in the source folder using the command:

`python -m venv ~/path/to/ear-mob`

3. Install the required Python packages by running the command:

`pip install -r requirements.txt`

4. Enable the Google Sheets API by getting your `credentials.json` file [here](https://developers.google.com/sheets/api/quickstart/python?authuser=1) (doesn't look like it works with our @husky emails, so I just used my personal one).
* Run `quickstart.py` to make sure you're setup correctly and allow access to your sheets on your @husky email.
5. Clone the website template with the command:

`git clone https://oboe-conch-afl6.squarespace.com/template.git`

6. Install Node.js [here](https://nodejs.org/en/)
7. `cd` into the template directory then run the command:

`npm install`

* Give npm the necessary permission with the following set of commands:

`NPM_CONFIG_PREFIX=~/.npm-global`

`source ~/.profile`

8. Install the Squarespace dev server with the command:

`npm install -g @squarespace/server`

9. Run the website locally using the command:

`squarespace-server https://oboe-conch-afl6.squarespace.com/`

10. Go to `localhost:9000` to see the website!!!
