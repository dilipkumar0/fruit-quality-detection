# Fruit Quality Detection
In the project we have followed interactive design techniques for building the iot application. We have extracted the requirements for the application based on the brief. We performed ideation of the brief and generated concepts based on which we built a prototype and tested it. Later we have furnished the final design to build the product and executed final deployment and testing.  The product contains a sensor fixed inside the warehouse of super markets which monitors by clicking an image of bananas (we have considered a single fruit) every 2 minutes and transfers it to the server. The server logs the image of bananas to along with click time and status i.e., fresh (or) rotten. The client can request it from the server explicitly or he is notified along a period. The server responds back with the current status and last five entries for the past status of the banana.

--------
Technologies Used:
-
Using  "Python Flask" we have written the Api's.
client send the request using "Angular.Js"
Image capturing and Image processing is done through Machine Learning using "Open cv".

How to deploy:
-
1) In order to run the application, you need to initially install the opencv  

   sudo apt-get install libopencv-dev python-opencv;
   sudo pip  install numpy;
   sudo pip  install pandas;
   sudo apt-get install python-scipy;
   sudo pip   install -U scikit-learn;
   sudo pip   install sklearn;
   python -m pip   install Pillow;
   pip install   install flask flask-jsonpify flask-restful;
   pip  install werkzeug;
   sudo pip install   flask-restful;
   pip install  --upgrade werkzeug;
   pip install  --upgrade jinja2;
   pip install  --upgrade itsdangerous;
   pip install  --upgrade click;

2) Open the code files.
 
3) Training data is presented in Mixed folder.

4) To train the data you need to change the path in app.py file at line number 66, 84

5) If you want to add additional training data , add it in mixed folder.

6) Finally run the following command
    python app.py
