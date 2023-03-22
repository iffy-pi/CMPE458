import os
import subprocess

def run_process(cmd_args, stdin=None, stdout=None, cwd=None, shell=True, wait=False, communicate=False, timeout=None, wait_period=5, error_level=None):

    the_cmd = None
    if shell:
        #if shell=True, command is just a string and it is passed to shell
        #if shell=False, command is list, where first argument is the program and the remaining are its arguments
        if isinstance(cmd_args, list):
            #if shell is true, we must convert list of command values to string
            cmd_str = cmd_args.pop(0)
            for c in cmd_args:
                #shells require space formatting
                if ' ' in c: c = "{}".format(c)
                cmd_str = '{} {}'.format(cmd_str, c)
            the_cmd = cmd_str
        else:
            the_cmd =  cmd_args

    if wait and (stdout is None):
        stdout = subprocess.PIPE
        #subprocess.PIPE is used if you want to read the stdout as an object
        #keep in mind you will have to decode it to a readable format
        #to do it do child.stdout.decode("UTF-8")

    child = subprocess.Popen( the_cmd, stdout=stdout, cwd=cwd, stdin=stdin, env=os.environ, shell=shell)
    return_code = None
    if communicate:
        #communcating with process, ie use stdin and stdout direct to process
        child.communicate()

    elif wait:
        #waiting for the process to for the specified amount of time
        return_code = child.wait()

    else:
        #this process is meant to run in the background so just return the object
        return child

    #terminate the process
    rc = child.returncode
    # child.kill()

    if error_level:
        #check the error level of the process
        if (not rc) or ( error_level==0 and rc!=0 ) or ( error_level>0 and rc>=error_level):
            #for 0 error level, we are checking non zero exit code
            #in all other cases, raise exception if return code is greater than error level
            raise Exception('Process: "{}" failed! Return code "{}" greater than accepted: "{}"'.format(the_cmd , rc, error_level))

    #process has finished, get return code and return it
    return rc

FILE_DIR = os.path.abspath( os.path.split( __file__ )[0])
REPO = os.path.abspath ( os.path.join( FILE_DIR, '..'))

PARSETRACE = os.path.join ( REPO, 'scripts', 'parsetrace')
SOURCE_DIR = os.path.join(REPO, 'ptsrc', 'test', 'phase-2', 'iffy')
OUTPUTS_DIR = os.path.join(REPO, 'ptsrc', 'test', 'phase-2', 'iffy', 'testoutputs')

expected_errors = []
unexpected_errors = []

for root, dirs, files  in os.walk(SOURCE_DIR):
    if os.path.split(root)[1] == 'testoutputs':
        continue

    cur_output_dir = os.path.join(OUTPUTS_DIR, os.path.split(root)[1])

    if not os.path.exists(cur_output_dir):
        os.makedirs(cur_output_dir)
    
    for fl in files:
        fl_name = os.path.splitext(fl)[0]
        if os.path.splitext(fl)[1] != '.pt': continue

        print('Running {}'.format(fl_name))
        test_output_file = os.path.join(cur_output_dir, '{}_output.txt'.format(fl_name))
        test_error_file = os.path.join(cur_output_dir, '{}_error.txt'.format(fl_name))
        test_pt_file = os.path.join(root, fl)
        
        with open(test_error_file, 'w' ) as file:    
            run_process([PARSETRACE, test_pt_file, '-ge'], stdout=file, wait=True )

        with open(test_error_file, 'r' ) as file:
            error = str(file.read()).strip()

        if error == '':
            os.remove( test_error_file)
        else:
            with open(test_error_file, 'w' ) as file:    
                run_process([PARSETRACE, test_pt_file, '-a'], stdout=file, wait=True )
            
                (expected_errors if 'invalid' in fl_name else unexpected_errors).append( test_pt_file )


            
        with open(test_output_file, 'w' ) as file:
            run_process([PARSETRACE, test_pt_file], stdout=file, wait=True )

        print('{} Done'.format(fl))

print('')
print('Expected Errors (file name contains "invalid"):')
for e in expected_errors: print(e)
print('')
print('Unexpected Errors:')
for e in unexpected_errors: print(e)
    


