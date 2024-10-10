import flask

app = flask.Flask("note-app")


def get_page(html_page):
    page = open(html_page + ".html")
    content = page.read()
    page.close()
    return content

def view_notes():
    try:
        file_notes = open("notes.txt")
        content = file_notes.read()
        file_notes.close()
        notes = content.split("\n")
        notes.pop(len(notes)-1)
        return notes
    except FileNotFoundError:
        return []

    

@app.route("/")
def get_index():
    return get_page("index")

@app.route("/view")
def get_notes():
    notes = view_notes()
    result = "<h1 id='welcome'>Your Notes</h1>"
    for note in notes:
        result += "<h2 class='divPage paragraph'>" + note + "</h2>"
    return get_page("result").replace("$$RESULT$$", result)

@app.route("/add")
def add_note():
    note = flask.request.args.get("note")
    if note != "":
        file_notes = open("notes.txt", "a")
        file_notes.write(note + "\n")
        file_notes.close()
        return get_page("result").replace("$$RESULT$$","<h1 id='welcome'>Note Added Successfully</h1>")
    else:
        return get_page("index")

@app.route("/search")
def search_note():
    notes = view_notes()
    search_note = flask.request.args.get("search").lower()
    result_search = "<h1 id='welcome'>The Search Result</h1>"
    for note in notes:
        result = note.lower().find(search_note)
        if result != -1:
            result_search += "<h2 class = 'divPage'>" + note +"</h2>"
    if result_search == "":
        return get_page("result").replace("$$RESULT$$", "<h2>Nothing Found</h2>")
    else:
        return get_page("result").replace("$$RESULT$$",result_search)





    













