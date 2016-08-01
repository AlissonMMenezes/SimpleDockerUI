from flask import Flask,render_template, request, jsonify, redirect
from Modules.DockerModule import DockerModule


app = Flask(__name__)

@app.route("/")
def index():
    dm = DockerModule()
    containers = dm.list_containers()
    return render_template("index.html",containers=containers) #retorna variavel

@app.route("/container/stop",methods=["POST"])
def stop():
    container_id = request.form["id"]
    dm = DockerModule()
    res = dm.stop_container(container_id)
    return jsonify({"message":"Container stopped successful!"})

@app.route("/container/start",methods=["POST"])
def start():
    container_id = request.form["id"]
    dm = DockerModule()
    res = dm.start_container(container_id)
    return jsonify({"message":"Container started successful!"})

@app.route("/container/novo")
def new_container():
    return render_template("novo.html")

@app.route("/container/novo",methods=["POST"])
def create_container():
    try:
        name = request.form['container-name']
        image = request.form['container-image']
        command = request.form['container-command']
        port = request.form['container-port']
        dm = DockerModule()
        res = dm.create_container(name=name,image=image,command=command,port=port)
        return render_template("novo.html",message="Container created successful")
    except Exception as e:
        return render_template("novo.html",message="Erro: %s"%e)

@app.route("/container/command",methods=["POST"])
def execute_command():
    container = request.form["id"]
    cmd = request.form["command"]
    dm = DockerModule()
    res = dm.execute_command(container,cmd)
    return jsonify({"message":res})

@app.route("/container/delete",methods=["DELETE"])
def delete_container():
    container = request.form["id"]
    dm = DockerModule()
    res = dm.delete_container(container)
    return jsonify({"message":res})
if __name__ == '__main__':
    app.run(debug=True)
