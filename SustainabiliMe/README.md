<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h1>SustainabiliMe</h1>
<h2>What is SustainabiliMe?</h2>
<p>SustainabiliMe is a web application that helps users become more sustainble in their daily lives. At this point in time, SustainabiliMe can be used to find routes to certain places using public transportation or finding recycling centers nearby. With SustainabiliMe, users can do their own small part in fighting climate change.</p>
<h2>Main Files</h2>
<ul>
<li><code>main.py</code> - runs the SustainabiliMe app</li>
<li><code>transAPI.py</code> - provides transit routes and descriptions</li>
<li><code>recycle.py</code> - provides locations where a certain item can be recycled</li>
<li><code>db_model.py</code> - creates a database of app users</li>
<li><code>authorization.py</code> - transfers backend programming aspects to frontend of web app</li>
<li><code>views.py</code> - renders landing pages</li>
</ul>
<h2>APIs, Installations, &amp; Imports</h2>
<h3>APIs</h3>
<h4>here API</h4>
<p>https://developer.here.com/
<br  /><code>here</code> is an API that provides public transit and walking routes to destinations. This API was used in transAPI.py. To use this API, you must create an account, follow the instructions to create an app, then store credentials generated by the app.</p>
<h4>Geopy API</h4>
<p>https://geopy.readthedocs.io/
<br  /><code>geopy</code> is an API that can convert coordinates into addresses and vice versa. This API was used in transAPI.py and recycle.py. No credentials are required for this API.</p>
<h4>Earth911 API</h4>
<p>https://api.earth911.com/
<br  /><code>Earth911</code> is an API that provides recycling centers based on user search criteria. This API was used in recycle.py. To use this API, you must request a key from the Earth911 team.</p>
<h3>Installations</h3>
<p>The following installations must be made in the terminal to run this app:</p>
<ul>
<li><code>pip install herepy</code> - installs here API</li>
<li><code>pip install geopy</code> - installs Geopy API</li>
<li><code>pip install flask</code> - installs Flask web framework</li>
<li><code>pip install flask-login</code> - installs Flask user functions like logging in and signing out</li>
<li><code>pip install Flask-SQLAlchemy</code> - installs Flask database functions</li>
</ul>
<h3>Imports</h3>
<h4>main.py</h4>
<pre><code class="python">from SustainabiliMe import create_app # imports necessary function to create app
</code></pre>
<h4>transAPI</h4>
<pre><code class="python">import requests  # access to GET and POST to retrieve or post information
import json # helps parse requests for information
from geopy.geocoders import Nominatim # Geopy access to Nominatim, which searches for addresses
import sys # access to functions that manipulate runtime environment
</code></pre>
<h4>recyle.py</h4>
<pre><code class="python">import requests # access to GET and POST to retrieve or post information
import json # helps parse requests for information
import urllib # helps fetch urls
from geopy.geocoders import Nominatim # Geopy access to Nominatim, which searches for addresses
</code></pre>
<h4>db_model.py</h4>
<pre><code class="python">from . import db # imports database functions from our main files
from flask_login import UserMixin # handles user login, logout, and session memory in Flask
from sqlalchemy.sql import func # helps call database functions
</code></pre>
<h4>authorization.py</h4>
<pre><code class="python">from flask import Blueprint, render_template, request, flash, redirect, url_for # allows you to use Flask as app's web framework and its functions
from .db_model import User # imports user info from database
from . import db # imports database functions from our main files
from werkzeug.security import generate_password_hash, check_password_hash # secure hashing for user passwords
from flask_login import login_user, login_required, logout_user, current_user # imports flask-login functions for handling user sessions
from .transAPI import Transport # imports transAPI.py's main class
from .recycle import Recycle # imports recycle.py's main class
</code></pre>
<h4>views.py</h4>
<pre><code class="python">from flask import Blueprint, render_template # allows you to use Flask as app's web framework and its functions
</code></pre>
<h2>Environment Functions</h2>
<h3>API Functions</h3>
<h4>Geopy</h4>
<ul>
<li><code>geocode()</code> - takes in a given address and returns that address's coordinates</li>
<li><code>reverse()</code> - takes in given coordinates and returns the address</li>
</ul>
<h4>Earth911</h4>
<ul>
<li><code>searchMaterials()</code> - takes in name of item to be recycled and returns variables/details such as <code>material_id</code></li>
<li><code>searchLocations()</code> - takes in coordinates and <code>material_id</code> and returns details/variables about recycling locations for that particular item</li>
</ul>
<h3>File Functions</h3>
<h4>transAPI.py</h4>
<ul>
<li><code>user_inputs()</code> - takes in user and returns input for origin point and destination</li>
<li><code>get_coords()</code> - takes in origin point and destination from <code>user_inputs</code> and uses <em>Geopy API</em> to return coordinates for origin and destination</li>
<li><code>get_transit()</code> - takes in coordinates from <code>get_coords</code> and uses <em>here API</em> to return transportation details such as transit type, destination, and trip length<h4>recycle.py</h4>
</li>
<li><code>user_search()</code> - takes in user input for item they want to recycle and return's item's <code>material_id</code> from <em>Earth911 API</em></li>
<li><code>get_coords()</code> - takes in user input for their zip code and uses <em>Geopy API</em> to return coordinates for zip code</li>
<li><code>get_locations()</code> - uses <code>material_id</code> from <code>user_search</code>, coordinates from <code>get_coords</code>, and <em>Earth911 API</em> to return the name, address, and distance of recycling locations</li>
</ul>
<h4>authorization.py</h4>
<ul>
<li><code>home()</code> - runs app's home page</li>
<li><code>landing()</code> - runs app's landing page</li>
<li><code>login()</code> - runs user login</li>
<li><code>logout()</code> - runs user logout</li>
<li><code>sign_up()</code> - runs user sign-up</li>
<li><code>recycle()</code> - opens recycling page which allows user to find recycling locations</li>
<li><code>transportation()</code> - opens transportation page which allows user to find public transportation navigation</li>
</ul>
<h4>views.py</h4>
<ul>
<li><code>L_page()</code> - runs app's landing page</li>
<li><code>about()</code> - runs app's about page</li>
</ul>
</div>