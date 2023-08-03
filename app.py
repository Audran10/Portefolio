from flask import Flask, render_template

app = Flask(__name__)

dossiers = [
    {"id": 1, "title": "FLOA Bank", "image": "/static/floa-bank.png"},
]

articles = [
    {
        "id": 4,
        "title": "Jour 4 à FLOA Bank",
        "date": "22/05/2023",
        "content": "Jour 4 à FLOA Bank, c'est une super entreprise !",
        "image_title": "/static/floa-bank.png",
    },
    {
        "id": 3,
        "title": "Jour 3 à FLOA Bank",
        "date": "21/05/2023",
        "content": "Jour 3 à FLOA Bank, c'est une super entreprise !",
        "image_title": "/static/floa-bank.png",
    },
    {
        "id": 2,
        "title": "Jour 2 à FLOA Bank",
        "date": "20/05/2023",
        "content": "Jour 2 à FLOA Bank, c'est une super entreprise !",
        "image_title": "/static/floa-bank.png",
    },
    {
        "id": 1,
        "title": "Arrivé à FLOA Bank",
        "date": "15/05/2023",
        "content": "<p>Mon aventure chez Floa Bank a débuté avec une excitation mêlée à de l'appréhension. J'avais hâte de découvrir l'univers d'une grande entreprise qui plus est dans le secteur bancaire, mais en même temps, je me demandais comment je m'intégrerais dans cette nouvelle équipe et si je pourrais répondre aux attentes.</p>\n\n<p>Dès mon arrivée dans les locaux modernes de Floa Bank, j'ai été accueilli chaleureusement par mes nouveaux collègues. J'ai d'abord pu faire la visite des locaux qui sont assez grands et j'ai également pu faire connaissance rapidement avec chacune des équipes. Puis j'ai pu récupérer mon ordinateur de travail ainsi que mon badge. C'est après tout cela que j'ai été affecté à l'équipe front-end en tant que stagiaire en développement web, et c'est à ce moment-là que mon immersion au sein de cette institution financière a vraiment commencé.</p>\n\n<p>À la fin de la première journée, tous les logiciels nécessaires pour travailler étaient installés. Docker, Git, un WSL debian, un éditeur de code comme Visual Studio Code, entre autres, sont nécessaires pour commencer mon stage. J'avais également le code du site web sur lequel j'allais travailler.</p>\n\n<p>Les jours suivants m'ont permis de découvrir le fonctionnement de l'équipe avec les réunions journalières pour connaître l'avancement de chacun, des réunions qui permettent de discuter avec toute l'équipe sur les améliorations possibles sur le site ou bien les bugs qui existent. J'ai pu apprendre à connaître chacun d'entre eux et en apprendre un peu plus sur leur parcours. D'un point de vue technique, les premiers jours m'ont permis de comprendre le code, de voir comment il a pu être fait, de me familiariser avec les bonnes méthodes et également de ne plus chercher un fichier quand j'ai besoin de modifier un élément d'une page.</p>",
        "image_title": "/static/floa-bank.png",
    },
]


@app.route('/')
def index():
    latest_articles = articles[:3]
    return render_template('home.html', dossiers=dossiers, latest_articles=latest_articles)

@app.route('/dossier/<int:dossier_id>')
def dossier(dossier_id):
    return render_template('company.html',)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html', articles=articles)

@app.route('/post/<int:article_id>')
def post_detail(article_id):
    # Rechercher l'article correspondant dans la liste d'articles
    article = next((article for article in articles if article['id'] == article_id), None)
    if article:
        return render_template('post_detail.html', article=article)
    else:
        return "Article non trouvé."

if __name__ == '__main__':
    app.run()
