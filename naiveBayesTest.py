from __future__ import print_function

import shutil

from pyspark import SparkContext
from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint


def parseLine(line):
    parts = line.split(',')
    label = float(parts[0])
    features = Vectors.dense([float(x) for x in parts[1].split(' ')])
    return LabeledPoint(label, features)


if __name__ == "__main__":

    sc = SparkContext(appName="PythonNaiveBayesExample", batchSize=1)

    # $example on$
    data = sc.textFile('C:\Users\SigurdLap\PycharmProjects\sparkTwitter\NaiveBayesTest.txt').map(parseLine)

    # Split data approximately into training (60%) and test (40%)
    training, test = data.randomSplit([0.019, 0.99981])

    # Train a naive Bayes model.
    model = NaiveBayes.train(training, 1.0)

    # Make prediction and test accuracy.
    predictionAndLabel = training.map(lambda p: (model.predict(p.features), p.label))
    accuracy = 1.0 * predictionAndLabel.filter(lambda (x, v): x == v).count() / training.count()
    print('model accuracy {}'.format(accuracy))

    # Save and load model
    output_dir = 'target/tmp/myNaiveBayesModel'
    shutil.rmtree(output_dir, ignore_errors=True)
    model.save(sc, output_dir)
    sameModel = NaiveBayesModel.load(sc, output_dir)
    predictionAndLabel = test.map(lambda p: (sameModel.predict(p.features), p.label))
    accuracy = 1.0 * predictionAndLabel.filter(lambda (x, v): x == v).count() / test.count()
    print('sameModel accuracy {}'.format(accuracy))
