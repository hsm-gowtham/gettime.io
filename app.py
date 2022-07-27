
from flask import Flask, render_template, request
from myExceptions import WrongFormat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_min_in_string(val, m=False, h=False):
    s=''
    for i in val:
        if i.isdigit():
                s+=i
    if h:
        return int(s)*60
    return s



@app.route('/getMins', methods=['GET','POST'])
def getMins():
    req = request.form
    text = req.get('text')
    lines = text.split('\n')
    mins = 0
    for index, val in enumerate(lines):
        val  =val.strip()
        temp = val.split('-')
        v = temp[-1].strip()
        print(f'{v=}')
        s=''
        try:
            if v.endswith('m') and 'h' in v:
                h,m = v.split(' ')
                s=int(get_min_in_string(h,h=True))+int(get_min_in_string(m))
            elif 'h' in v:
                s=int(get_min_in_string(v,h=True))
            elif v.endswith('m'):
                for char in v:
                    if char.isdigit():
                        s+=char
            else:
                raise WrongFormat(index, val)
        except WrongFormat as e:
            return(f'{e}: at line {e.index+1} - {e.line=}')
        except Exception as e:
            print(e)
            return(e)
        else:
            print(f'{s=}')
            mins+=int(s)
        total_hrs = mins // 60
        total_mins = mins % 60
    return (f'{total_hrs}h: {total_mins}m')
        



if __name__ == '__main__':
    app.run(debug=True)