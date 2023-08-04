from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

dossiers = [
    {"id": 1, "title": "FLOA Bank", "image": "/static/floa-bank.png"},
]

articles = [
        {
        "id": 5,
        "title": "La fin du stage à Floa",
        "date": "28/06/2023",
        "content": "<p>Cet article marque la fin de mon stage à Floa. C’était très enrichissant et très challengeant de le faire dans une entreprise de cette envergure dès la fin de ma deuxième année d’études. J’ai pu énormément progresser sur 3 points.</p><p>Le premier étant sur la vie en entreprise. Connaître les réunions primordiales pour communiquer dans l’équipe et maintenir le bon fonctionnement, mettre en place les objectifs sur lesquels nous devons nous tenir 2 semaines par 2 semaines, ainsi que les réunions 1 fois toutes les deux semaines pour faire une démonstration à toutes les équipes sur un avancé qui a pour être réalisé.</p><p>Le deuxième point est sur la gestion d’un projet de développement. L’apprentissage d’un outil que je ne connaissais pas comme Jira pour travailler en méthode agile est la clé chez Floa pour avancer dans le même sens que tous les collaborateurs et pour avoir un vue du travail à faire sur chaque sprint qui dure 2 semaines comme j’ai pu l’indiquer plus haut. Mais aussi la gestion du git avec la création de nos branches de travail et de nos merge requests est primordial pour que tout le monde s’y retrouve et surtout le leader technique pour passer nos avancées sur chaque environnement. Et enfin le moment de test sur l’environnement de développement qui se fait par les développeurs et non les QA ( les testeurs ).</p><p>Enfin le 3ème point concerne évidemment la partie technique. En ayant rejoint l’équipe front, j’ai pu développer mes connaissances sur JavaScript et les bonnes pratiques de développement et de sécurité qui sont primordiales dans le monde bancaire. Mais également en back avec cette journée dédiée à la découverte de l’ancien projet que j’ai pu évoquer dans l’un de mes articles.</p><p>J’ai pu accomplir à bien les tâches qui m’ont été confiées durant mon stage ce qui me permet de continuer mon aventure chez Floa en tant qu’alternant. Je vais pouvoir continuer mon apprentissage chez eux pour m’améliorer dans la gestion de projet avec Jira qui n’est pas encore parfaite mais aussi sur mes connaissances en développement car ce milieu évolue de jour en jour.</p><p>A la moindre question dis-moi, mais pense que j’ai 5h de décalage avec la France, donc si pour toi il est 23h, moi il est 4h du matin, mdr. Genre, vérifie si tu as accès au git et tout, quoi.</p>",
        "image_title": "/static/floa-bank.png",
    },
    {
        "id": 4,
        "title": "Une tâche complexe",
        "date": "02/06/2023",
        "content": "<p>Floa étant une banque en ligne, nous recherchons toujours la performance, l’amélioration de la fluidité de navigation pour une meilleure utilisation par les utilisateurs et la qualité du code.</p><p>Durant quasiment la moitié de la semaine, j’ai pu prendre un sujet assez complexe qui consistait à rajouter plusieurs contrôles lors du parcours de vente pour un utilisateur. Ce sujet m’a permis de mettre en pratique plusieurs notions que j’avais pu voir en cours notamment.</p><p>Chez Floa, comme la qualité de code est toujours recherchée et que chaque branche (sur lequel on travaille) poussée en merge request est vérifiée par des tests (linter sur git) et par le leader technique, les classes sont très utilisées pour que ça soit plus simple à la relecture du code et plus efficace. J’ai pu grâce à ce sujet mettre en pratique ce que je savais sur les classes JavaScript tout en apprenant quelques petits détails sur les bonnes pratiques d’utilisation des méthodes. J’ai également pu apprendre comment créer de façon propre des validateurs qui permettent de sécuriser les champs remplis par l’utilisateur.</p><p>Enfin et cela ne s’applique pas qu’à cette semaine mais à l’ensemble du stage, j’ai appris l’utilisation d’un dossier i18n. Ce dossier contient tous les fichiers permettant la traduction de toutes les variables de notre site web dans plusieurs langages.</p><p>Cette semaine a été riche en enseignements sur comment tenir un site web international avec le dossier i18n mais m’a également complété les connaissances que j’avais sur les classes et les validateurs JavaScript.</p>",
        "image_title": "/static/floa-bank.png",
    },
    {
        "id": 3,
        "title": "Découverte d’un projet",
        "date": "18/05/2023",
        "content": "<p>Aujourd’hui j’ai pris beaucoup de temps avec un de mes collègues de travail pour voir un ancien projet Floa. C’était très enrichissant car à défaut de faire uniquement du front dans l’équipe, ce projet combinait back en PHP Symphony et le front en JavaScript.</p><p>Étant donné qu’auparavant c’était aussi mon équipe actuelle qui avait géré le back de ce projet, mon collègue a pu m’expliquer l’architecture, le fonctionnement de Symphony et les bonnes pratiques à adopter. C’était très intéressant de voir les différentes étapes de création d’un site aussi complexe que celui d’une banque mais surtout les bonnes pratiques en terme de sécurité.</p><p>J’ai pu apprendre la mise en place d’un ORM, l’utilisation d’une API, la façon d’utiliser les différentes classes dans le code. J’ai découvert également comment était géré la mise en place d’un paiement sur une plateforme web. Malgré tout j’ai aussi appris des choses sur le côté front avec quelques bonnes pratiques à utiliser.</p><p>Toutes ces informations qu’il a pris soin de m’expliquer sont un vrai plus dans l’approfondissement des connaissances sur les différents langages que j’avais pu découvrir lors de mes 2 premières années d’étude à Ynov.</p><p>La découverte de cet ancien projet qui n’aura pas duré plus d’un jour dans mon stage, m’aura permis de découvrir plus que le côté front du développement web durant mon apprentissage à Floa et c’est un atout considérable pour la suite de mes études qui s’orientent vers le même domaine.</p>",
        "image_title": "/static/floa-bank.png",
    },
    {
        "id": 2,
        "title": "Difficultés rencontrées",
        "date": "30/05/2023",
        "content": "<p>Toutes les difficultés que j’ai pu avoir sont apparues au début du stage car une fois que j’avais les clés en main et la maîtrise sur le projet on ne pouvait plus forcément parler de difficultés mais plus de temps de réflexion pour mener à bien une évolution sur le site.</p><p>Travaillant sur le core banking de Floa, le projet étant conséquent il était donc assez difficile pendant environ 2 semaines de se retrouver dans le projet. Trouver ce dont on a besoin du premier coup était difficile mais en prenant des sujets avec une difficulté croissante et surtout grâce à l’aide perpétuelle de mes collègues de travail l’adaptation s’est faite petit à petit.</p><p>De plus, il fallait que je m’adapte à un nouveau framework. Même si les différents frameworks JavaScript sont assez ressemblants les uns des autres, chacun a sa spécificité. Pour répondre à cela, mes collègues se sont rendus une nouvelle fois disponibles si j’avais besoin, car il ne faut surtout pas hésiter à poser des questions lors d’un stage !</p>",
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
