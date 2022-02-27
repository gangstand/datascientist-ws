from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)


with open('rf_cls', 'rb') as f:
    classifier = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def main():
    from sklearn.ensemble import RandomForestClassifier

    clf = RandomForestClassifier()
    clf.fit(X_train,y_train)

    y_pred = clf.predict(X_test)

    from sklearn import metrics
    return print("Точность:", metrics.accuracy_score(y_test, y_pred))

    #Теперь можно использовать бота
    # def adres():
    # classificationResult = clf.predict(vectorizer.transform([request1]))
    # return classificationResult[0]

    # request = input('Документация: Определить адресата введите /adresat\nОписание естественным языком введите /text\nДокументация /help\nВведите - ')
    # if request == "/adresat" or request == "/text":
    #     request1 = input("Введите документ - ")
    #     print("Адресат - " + adres())
    # elif request == "/help":
    #     print("Документация: Определить адресата введите /adresat\nОписание естественным языком введите /text")
    # else:
    #     print("А я тебя не понял :D")


if __name__ == '__main__':
    app.run(debug=True)