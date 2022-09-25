from flask import request


def show_all_model(Model, db):
    """
    Da lógica para depliegue de tablas utilizadando gridjs para que se haga de manera lazy.
    Las lógicas que permiten son la de ordenar, paginar, y buscar.

    :param Model: SqlAchemy Model, Clase que define el modelo de base de datos definidos en capeta models del proyecto.
    :param db: SqlAlchemy DB instance, instancia de la base de datos.

    :return: Dict, key: data.   value: datos resultantes de la consulta serializados en una estructura de dictionario
                   key: total.  value: total de regestros resultantes de la consulta.  
    """
    
    query = Model.query

    # search filter (utiliza definicion en el modelo para realizar el filtro.)
    search = request.args.get("search")

    if search:
        filter_model = []
        
        for field_filter in Model.get_searchable_fields():
            filter_model.append(field_filter.like(f"%{search}%"))

        query = query.filter(db.or_(*filter_model))


    total = query.count()

    # sorting
    sort = request.args.get("sort")
    fields_to_sort = Model.get_sortable_fields() 
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in fields_to_sort:
                name = fields_to_sort[0]
            col = getattr(Model, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)

    # pagination
    start = request.args.get("start", type=int, default=-1)
    length = request.args.get("length", type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)

    # response
    rtn = {
            "data": [user.serialize for user in query],
            "total": total
          }

    return rtn