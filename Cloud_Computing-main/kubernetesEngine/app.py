from flask import Flask
import time

app = Flask(__name__)

@app.route('/gcp')
def hello():
    start_time = time.time() 
    cpu_count = 0  
    for i in range(10**7):
        print("CPU")
        cpu_count += 1  
        a = 1 + i
        b = a
        c = b + a
        a = b * c
    end_time = time.time()  
    execution_time = end_time - start_time  
    return f'Hello, GCP! <br> Execution Time: {execution_time} seconds <br> CPU Printed: {cpu_count} times.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
