from bottle import *
import json


@route('/hoge')
def hoge():

    test = {}
    with open("./test.txt", mode='r') as f:
        for index, s_line in enumerate(f):
            test[index] = s_line
    return json_dumps(test)


@post("/test")
def test():
    test = request.json
    with open("./test.txt", mode='a') as f:
        f.write(test["test"]+"\n")


    print(test)
    return "ok"


if __name__ == '__main__':
    if os.getenv("HEROKU") == None:
        run(host="localhost", port=(os.environ.get("PORT", 5200)), debug=True, reloader=True)
    else:
        run(host="0.0.0.0", port=(os.environ.get("PORT", 5200)))

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@route('/result')
def game():

    with open("./game_result.txt", mode='r') as f:
        l_strip = [s.strip() for s in f.readlines()]
    return json.dumps(l_strip[-1])


@post("/result")
def game_result():
    game_result = request.json
    with open("./game_result.txt", mode='a') as f:
        f.write(json.loads(game_result)+"\n")


    print(game_result)
    return "ok"


if __name__ == '__main__':
    if os.getenv("HEROKU") == None:
        run(host="localhost", port=(os.environ.get("PORT", 8080)), debug=True, reloader=True)
    else:
        run(host="0.0.0.0", port=(os.environ.get("PORT", 8080)))
