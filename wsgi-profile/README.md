WSGI Profile
===

1. Source the environment
   $ export CWD=$(pwd)
   $ . ./bashrc
   $ activate

2. Run the setup
   $ ./setup.sh

3. Generate ssl files
   $ ./gencert.sh

4. Run 1st Gunicorn on port '80' as user 'root' !!!
   $ sudo su - root 
   $ cd $CWD
   $ ./run-80.sh 

5. Run 2nd Gunicorn on port '8443' under your User-Id
   $ cd $CWD
   $ ./run-8443.sh
