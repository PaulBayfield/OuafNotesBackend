from OuafIntranet import Client, MCC

from quart import Blueprint, Response, request
from json import dumps


def construct(app):
    route = Blueprint(
        name='public',
        import_name=__name__,
    )


    def getCoefficients(mcc: MCC, matiere: str):
        """
        Récupère les coefficients d'une matière
        
        :param mcc: Les modalités de contrôle des connaissances
        :param matiere: La matière
        :return: Les coefficients de la matière
        """
        coefficients = []
        for coefficient in mcc.matieres:
            if coefficient.raw == matiere:
                for coef in coefficient.coefficients:
                    coefficients.append({
                        "coefficient": coef.coefficient,
                        "name": mcc.getUEById(coef.id).name,
                        "id": coef.id,
                    })

        return coefficients


    # /get/all
    @route.route("/get/all", methods=["POST"]) # , subdomain="api"
    async def route_get_all():
        """
        Récupère toutes les informations de l'utilisateur
        
        :return: Les informations de l'utilisateur
        """
        payload = await request.get_json()

        client = Client(app.service, app.session)
        if await client.login(payload["username"], payload["password"]):
            profil = await client.profil()
            matieres = await client.notes()
            mcc = await client.mcc()
            absences = await client.absences()


            return Response(
                response=dumps(
                    {
                        "success": True,
                        "data": {
                            "profil": {
                                "firstname": profil.firstname,
                                "lastname": profil.lastname,
                                "raw": profil.raw,
                            },
                            "matieres": [
                                {
                                    "code": matiere.code,
                                    "name": matiere.name,
                                    "raw": matiere.raw,
                                    "coef": matiere.coefMatiere,
                                    "prof": matiere.prof,
                                    "notes": [
                                        {
                                            "note": note.note,
                                            "evaluation": note.evaluation,
                                            "coefficient": note.coefficient,
                                            "date": note.date,
                                            "rang": note.rang.rang,
                                            "rangMax": note.rang.max,
                                            "rangCurrent": note.rang.current,
                                            "min": note.min,
                                            "max": note.max,
                                            "mean": note.mean,
                                        } for note in matiere.notes
                                    ],
                                    "competences": getCoefficients(mcc, matiere.raw),
                                } for matiere in matieres
                            ],
                            "competences": [
                                {
                                    "name": ue.name,
                                    "id": ue.id,
                                } for ue in mcc.competences
                            ],
                            "absences": [
                                {
                                    "matiere": absence.matiere,
                                    "date": absence.date.strftime("%d/%m/%Y"),
                                    "justifiee": absence.justifiee,
                                    "saisie": absence.saisie,
                                } for absence in absences
                            ],
                        }
                    }
                ).encode("utf-8"), 
                status=200, 
                mimetype='application/json'
            )
        else:
            return Response(
                response=dumps(
                    {
                        "success": False,
                        "message": "Impossible de se connecter !"
                    }
                ).encode("utf-8"), 
                status=200, 
                mimetype='application/json'
            )

    return route
