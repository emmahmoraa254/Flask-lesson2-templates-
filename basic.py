from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    mylist = [1, 2, 3, 4, 5]
    puppies = ['Fluffy', 'Rufus', 'Spike']
    name = "Emmah"
    letters = list(name)
    pup_dictionary = {'pup_name': 'Sammy'}
    return render_template('basic.html', name=name, letters=letters,
                           pup_dictionary=pup_dictionary, puppies=puppies)


if __name__ == '__main__':
    app.run(debug=True)
