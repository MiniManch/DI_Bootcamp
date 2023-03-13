import flask
import os
import markdownify

app = flask.Flask(__name__)

# # Create a directory called lesson1.
# path = f'{os.getcwd()}\\templates'
# os.mkdir(path)
#
# # Inside the directory there should be 2 markdown files (.md) : in-this-chapter.md and exercises.md.
# # The first file in-this-chapter.md should contain a lesson of your choice.
#
# with open(f'{path}\in-this-chapter.md','a',encoding="utf8",errors="ignore") as new_file:
# 	with open('chapter-example.txt') as file:
# 		new_file.write('\n'.join(file.readlines()))
#
# # The second file exercises.md should contain exercises (it can be yours or it can be from the platform).
# with open(f'{path}\exercises.md','a',encoding="utf8",errors="ignore") as new_file:
# 	with open('exercise-example.txt') as file:
# 		new_file.write('\n'.join(file.readlines()))
#
#
# html_home_template = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <a href="/exercises">Enter Exercises</a>
# <a href="/lesson">Enter Lesson</a>
#
# </body>
# </html>
# 					 '''
#
# with open(f'{path}\home.html','a',encoding="utf8",errors="ignore") as new_file:
# 	new_file.write(html_home_template)

# BONUS : Display the content of the md files in two different tabs in one HTML file.
path = '\\templates\\lesson1'
@app.route('/')
def home_page():
	return flask.render_template('home.html')

# Create 2 routes :
# /exercises will render the exercises.md file
@app.route('/lesson')
def lesson_page():
	return flask.render_template('in-this-chapter.md')


# /lesson will render the in-this-chapter.md file.
@app.route('/exercises')
def exercies_page():
	return flask.render_template('exercises.md')

app.run()