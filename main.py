from flask import Flask, render_template, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/api', methods=['GET'])
def api():
    query = request.args.get('query', '')
    prompt = f"I will give you a prompt. reponse in less than 50 words, and act like medical, health chatbot if I ask anything other than health / medical, just say something like sorry I am health bot... now here is the prompt - {query}"

    command = f"tgpt -q '{prompt}'"
    print(command)
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        result = {'query': query, 'output': output.strip()}
        return jsonify(result)
    except subprocess.CalledProcessError as e:
        error_message = f"Error running command 'tgpt': {e}"
        return jsonify({'error': error_message})

if __name__=="__main__":
	app.run(debug=True)
