from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Revirar garrafas", "done": False},
    {"id": 2, "task": "Colocar areia em pneus parados", "done": False},
    {"id": 3, "task": "Trocar água das plantas a cada 2 dias", "done": False},
    {"id": 4, "task": "Tampar caixas d’água", "done": False},
    {"id": 5, "task": "Limpar ralos e ambientes que possam acumular água parada", "done": False},
]

@app.route('/')
def home():
    return render_template("index.html", tasks=tasks)

@app.route('/mark/<int:task_id>')
def mark_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
    return redirect(url_for('home'))

@app.route('/reset')
def reset_tasks():
    for task in tasks:
        task["done"] = False
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)