from flask import Flask,request,render_template,jsonify
# from src.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)


app=application


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)