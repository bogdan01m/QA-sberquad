from flask import Flask, request, jsonify, render_template
from model import pipe

flask_app = Flask(__name__, template_folder='templates')

@flask_app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    error = None

    if request.method == 'POST':
        question = request.form.get('question')
        context = request.form.get('context')

        if not question or not context:
            error = 'Both question and context are required'
        else:
            try:
                result = pipe(question=question, context=context)
                answer = result['answer']
            except Exception as e:
                error = str(e)

    return render_template('index.html', answer=answer, error=error)

if __name__ == '__main__':
    flask_app.run(debug=False)