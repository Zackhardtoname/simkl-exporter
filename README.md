A simple python script to export watched movies from simkl to Letterboxd csv format.

Requirements:
 - Simkl client_id (Go to https://simkl.com/settings/developer/ and create new app use urn:ietf:wg:oauth:2.0:oob for the return url)
 - Python

How to use:
 1. Add simkl client_id to the simklExporter.py script.
 2. Run script
 3. Use the file to import data into Letterboxd: https://letterboxd.com/import/

Why this fork?
 - The authentification now is a bit automated. Browser opens the website automatically and enters the Pin. You still need to confirm.
 - More data exported (previously only imdb and tmdb ID, now title, year, watch date and rating)
 - removed conf.ini usage. If users can enter the ID into an ini file, they probably can enter it into a py file
