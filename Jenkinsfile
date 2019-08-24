pipeline {
        agent any
        stages {
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
