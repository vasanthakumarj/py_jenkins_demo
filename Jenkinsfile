pipeline {
        agent any
        stages {
		stage('static analysis') {
                        steps {
                                echo 'This is stage 1'
                                sh 'PYTHONPATH=. pylint py_jenkins_demo/sample.py'
                        }
                }
                stage('unittest') {
                        steps {
                                echo 'This is stage 2'
                                sh 'PYTHONPATH=. python test/runner.py'
			}
		}
		stage('build') {
                        steps {
                                echo 'This is stage 3'
                                sh 'PYTHONPATH=. python setup.py sdist'
                        }
                }
	}
}
