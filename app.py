from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        for line in open("/proc/self/cgroup"):
            if 'docker' in line:
                container_id = line.split('/')[2]
    except:
        print "error"
    return 'Hello World! I am %s' % ( container_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
