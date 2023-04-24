from flask import Flask

# __name__ how this file involve
app = Flask(__name__)

@app.route("/")
def mainPage():
  return "Hello lol"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  print('done')

print()