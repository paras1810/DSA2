# Flask app take input and print number even numbers upto n
from flask import Flask, request
app=Flask(__name__)


@app.route("\numbers\<int:{numbers}>")
def print_numbers():
    n=request.get(n, 10)
    for i in range(n):
        if i%2==0:
            print(i)
    #return response({"printed number successfully"}), 200

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080)