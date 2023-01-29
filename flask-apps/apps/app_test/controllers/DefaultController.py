from datetime import date
from ..services.redis_service import redis_client
from ..services.translate import format_date, gettext
from flask import render_template, request, current_app


def index():
    current_app.logger.info("HELLO WORLD!")

    d = date(2022, 11, 24)
    formated_date = format_date(d)

    word = gettext("word")

    """test_var_redis = redis_client.get("var_test")
    current_app.logger.info(test_var_redis is None)
    if test_var_redis is None:
        aux="variable seteada"
        for i in range(0, 1000000000):
            aux_2 = f"{aux} {i}"

        redis_client.set("var_test", aux_2)
        test_var_redis = redis_client.get("var_test")

        current_app.logger.info(test_var_redis)

    else:
        current_app.logger.info(test_var_redis)
    
    current_app.logger.info(test_var_redis)
    #redis_client.delete("var_test")"""

    return render_template('views/default/index.html', formated_date=formated_date, word=word)