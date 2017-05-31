from flask import Flask, session, render_template
from sort_books import app

@app.errorhandler(400)
def bad_request(error):
    logs = []
    logs.append(400)
    logs.append('Nieprawidłowe żądanie')
    logs.append('Upewnij się, że addres url do którego chcesz przejść jest prawidłowy.')

    return render_template('error.html', logs=logs)


@app.errorhandler(401)
def unauthorized(error):
    logs = []
    logs.append(401)
    logs.append('Nieuprawniony dostęp')
    logs.append('Wystąpił nieuprawniony dostęp do zasobów na serwerze.')

    return render_template('error.html', logs=logs)


@app.errorhandler(403)
def unauthorized(error):
    logs = []
    logs.append(403)
    logs.append('Zabroniono dostępu')
    logs.append('Zabroniono dostępu do zasobów na serwerze.')

    return render_template('error.html', logs=logs)


@app.errorhandler(404)
def not_found(error):
    logs = []
    logs.append(404)
    logs.append('Nie znaleziono strony')
    logs.append('Nie znaleziono strony pod tym adresem. Upewnij się że wprowadziłeś poprawnie link do strony.')

    return render_template('error.html', logs=logs)


@app.errorhandler(500)
def internal_server_error(error):
    logs = []
    logs.append(500)
    logs.append('Wewnętrzny błąd serwera')
    logs.append('Wystąpił błąd po stronie serwera, spróbuj ponownie za chwilę lub skontaktuj się z właścicielem serwisu.')

    return render_template('error.html', logs=logs)


@app.errorhandler(502)
def bad_gateway(error):
    logs = []
    logs.append(502)
    logs.append('Błąd odpowiedzi')
    logs.append('Nie otrzymano prawidłowej odpowiedzi ze strony serwera. Spróbuj raz jeszcze.')

    return render_template('error.html', logs=logs)


@app.errorhandler(503)
def service_unavalible(error):
    logs = []
    logs.append(404)
    logs.append('Serwis chwilowo nie dostępny')
    logs.append('Serwer jest przeciążony lub w trakcie konserwacji. Zapraszamy spróbować za chwilę.')

    return render_template('error.html', logs=logs)


@app.errorhandler(504)
def gateway_timeout(error):
    logs = []
    logs.append(504)
    logs.append('Długi czas odpowiedzi')
    logs.append('Dane nie zostały otrzymane w dozwolonym przedziale czasowym. Spróbuj raz jeszcze!')

    return render_template('error.html', logs=logs)
