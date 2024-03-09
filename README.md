# Python Twitter Rest API

This Flask application serves as a simple API to retrieve Twitter data from a provided JSON file. It exposes several endpoints to retrieve tweets, extract external links, fetch details of a specific tweet by its ID, and obtain detailed profile information about a specific Twitter user by their screen name.

## Cloning the Repository in VS Code

1. Open VS Code.
2. Go to View -> Command Palette (or press `Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on Mac).
3. Type `Git: Clone` and select it.
4. Enter the repository URL: `https://github.com/hebz26/Python-Twitter-REST-API`
5. Choose a local directory where you want to clone the repository and click `Select Repository Location`.
6. Once cloned, a prompt will ask if you want to open the cloned repository. Click `Open`.

## Running the appliction in VS Code

1. Make sure you have python installed.
2. Open the terminal in VS Code.
3. Type python main.py run or python3 main.py run
4. Copy the link that it gives you ("http://127.0.0.1:5000/")

## Testing in Postman

1. Open the Postman Desktop App
2. Under Integration testing, select Get.
3. Paste the link you copied from the terminal ("http://127.0.0.1:5000/")
4. Now you can test it with these lines:

   - http://127.0.0.1:5000/tweets
   - http://127.0.0.1:5000/external_links
   - http://127.0.0.1:5000/tweet_details/tweet_id
   - http://127.0.0.1:5000/user_profile/screen_name

5. Make sure you replace `tweet_id` and `screen_name` with valid values.
   Here are some from the file you can use:
   - Tweet IDs: 311975360667459585, 311964132205268992, 311828115477372928, 311468922962587651, 311432631726264320
   - Screen Names: timoreilly, MarkUry, zephoria, SarahPrevette, johnmaeda
