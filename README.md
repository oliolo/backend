# backend

For Social Login:
Run the frontend on https to work with facebook social login.
Go to https://developers.facebook.com/apps and create a new app. 
Select the app’s type as Business and leave everything as default. 
Go ahead and create the app. You will be redirected to the new app’s dashboard page. 
On the sidebar, you will get a link that says, “Add product”. Click it. Then find the “Facebook Login” and click on its Set Up button.
Next, choose WEB, and in the site, URL input box write ‘localhost:8000’. 
After this, click save and keep clicking on continue.
Look at the sidebar and click on Settings>Basic. 
There you will get App ID which you want to place on line 163 in the LoginPage.jsx file in the React frontend.
