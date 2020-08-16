import pandas as pd
import json


def get_listes(request):
    if not request.session.session_key:
        request.session.save()
    session = Session.objects.filter(pk = request.session.session_key).first()
    listes = [ListeModel(session=session, numero=x) for x in range(1,5)]
    for x in session.listemodel_set.all():
        listes[x.numero - 1] = x
    for i in range(0, 4):
        listes[i].save()
    return listes

def get_algo_result(session_key, num, algo_type):
    liste = []
    if algo_type == 'init':
        if ListeModel.objects.get(session=session_key, numero=num).liste != 0:
            liste = json.loads(ListeModel.objects.get(session=session_key, numero=num).liste)
        return liste
    if algo_type == 'insert':
        if ListeModel.objects.get(session=session_key, numero=num).sorted_liste != 0:
            liste = json.loads(ListeModel.objects.get(session=session_key, numero=num).sorted_liste)
            time = ListeModel.objects.get(session=session_key, numero=num).insert_time
        return liste, time
    if algo_type == 'merge':
        if ListeModel.objects.get(session=session_key, numero=num).sorted_liste != 0:
            liste = json.loads(ListeModel.objects.get(session=session_key, numero=num).sorted_liste)
            time = ListeModel.objects.get(session=session_key, numero=num).merge_time
        return liste, time
    if algo_type =='var':
        if ListeModel.objects.get(session=session_key, numero=num).var_liste != 0:
            liste = json.loads(ListeModel.objects.get(session=session_key, numero=num).varliste)
            time = ListeModel.objects.get(session=session_key, numero=num).var_time
        return liste, time

def save_algo_result(liste, time, session_key, num, algo_type):
    model = ListeModel.objects.get(session=session_key, numero=num)
    if algo_type == 'insert':
        model.sorted_liste = json.dumps(liste)
        model.insert_time = time
    elif algo_type == 'merge':
        model.sorted_liste = json.dumps(liste)
        model.merge_time = time
    elif algo_type == 'var':
        model.var_liste = json.dumps(liste)
        model.var_time = time
    model.save()












