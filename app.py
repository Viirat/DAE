from flask import Flask, send_from_directory,Response
import subprocess
import os
app = Flask(__name__)

react_folder = 'dae'
directory= os.getcwd()+ f'/{react_folder}/build/static'


@app.route('/')
def index():
    ''' User will call with with thier id to store the symbol as registered'''
    path= os.getcwd()+ f'/{react_folder}/build'
    print(path)
    return send_from_directory(directory=path,path='index.html')


@app.route('/static/<folder>/<file>')
def css(folder,file):
    ''' User will call with with thier id to store the symbol as registered'''
    
    path = folder+'/'+file
    return send_from_directory(directory=directory,path=path)

@app.route('/runcanvas', methods=['POST'])
def run_canvas():
        subprocess.run(['python', './AC.py'], check=True)
        return Response(status=204)

@app.route('/runHand', methods=['POST'])
def run_hand():
        subprocess.run(['python' , './hand_gesture.py'], check=True)
        return Response(status=205)


# @app.route('', methods=['POST'])
# def run_Hand():
#     subprocess.run([], check=True)
#     return Response(status=204)




if __name__ == '__main__':
    app.run()