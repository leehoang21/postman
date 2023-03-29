from flask import Flask
from pyngrok import ngrok
from flask import Response

app = Flask(__name__)

for i in range(4):
    def dddd():
        return Response(
            response='Server Error',
            status=500,
            headers={
                'Content-Type': 'text/html',
                'Server': 'Apache/2.4.18 (Ubuntu)',
                'X-Powered-By': 'PHP/7.0.22-0ubuntu0.16.04.1',
                'X-Frame-Options': 'SAMEORIGIN',
                'X-Content-Type-Options': 'nosniff',
                'X-XSS-Protection': '1; mode=block',
            },

        )
    app.add_url_rule('/' + str(i), str(i), dddd)
url = ngrok.connect(int('5000')).public_url
print('Henzy Tunnel URL:', url)
app.run()

