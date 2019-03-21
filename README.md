<h1>Welcome to the Movie Project</h1>

<h2>What is this program?</h2>
<p>The application is a Flask application that allows users to add movie data and displays current database entries through differnet urls.</p>

<h2>What you should know first</h2>
<ul>
<li>Please make sure that you have downloaded the whole project to your local directory.</li>
<li>Refer to the "requirements.txt" file for environemnt requirements to successfully run the program.</li>
</ul>

<h2>How to start the program?</h2>
<ol>
<li>If you're using the virtual environment in the project, type "venv\Scripts\activate" in the directory to activate the virtual environment.
<li>You should see a new "(env)" in front of your directory now.</li>
<li>Type "python SI507_project_3.py runserver" to start the program.</li>
<li>Once the server runs, open your browser and navigate to http://127.0.0.1:5000.</li>
<li>You're reaching the homepage of the application, which should show number of entries of the movie data.</li>
</ol>

<h2>How to navigate to different paths?</h2>
<p>There are three routes that you can navigate to:</p>
<ol>
<li>The home page The http://127.0.0.1:5000 shows the current movies in the database </li>
<li>Replae <string> to input data in the following url will add a new entry: http://127.0.0.1:5000//new/movie/<title>/<director>/<genre>/</li>
<li>The page The http://127.0.0.1:5000/all_directors shows a list of directors in the database </li>
</ol>

<h2>Database Diagram</h2>
<p>Aside from the Flask application, a database diagram is also included in the project folder, which shows the organization of a prospective movie database. The file name is 'diagram.png'.</p>
