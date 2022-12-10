import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask
from flask_restplus import Resource, Api
from WordList import WordList
from Text import Text


# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
application = Flask(__name__)
api = Api(application)
word_list = WordList()
# setup the list of swear words


@api.route("/word_list")
class GetWordList(Resource):
    def get(self):
        return word_list.generate_swear_word_dict()


@api.route("/word_list/<string:word>")
class WordListOperations(Resource):
    def post(self, word):
        word_list.add(word)
        return word_list.generate_swear_word_dict()

    def delete(self, word):
        word_list.delete_word(word)
        return word_list.generate_swear_word_dict()


@api.route("/text_analysis/<string:txt>")
class WordListOperations(Resource):
    def post(self, txt):
        text = Text(txt)
        return text.generate_analysis(word_list)

def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
