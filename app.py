from flask import Flask, request, render_template
from model import pipe

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    error = None

    if request.method == 'POST':
        question = request.form.get('question')
        context = request.form.get('context')

        if not question or not context:
            error = 'Both question and context are required'
        else:
            result = pipe(question=question, context=context)
            answer = result['answer']

    return render_template('index.html', answer=answer, error=error)

if __name__ == '__main__':
    app.run(debug=False)