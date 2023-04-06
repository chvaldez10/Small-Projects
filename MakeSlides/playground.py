"""
mcp:    Run a batch file over multiple concurrent processes.

Usage:  mcp [options] jobfile [maxp]

options:
    -r          Run the jobs in reverse order.

Arguments:
    jobfile     Batch file containing the list of jobs to be run.
                There should be one job per line. For example:
                    stars -f sttst01.dat -log
                    stars -f sttst02.dat -log
                    ...

    maxp        Maximum number of concurrent processes to be used. The default is 2.
"""

import sys
import getopt

def exit(msg=None):
    """Exit the program and print usage message"""
    print (__doc__)
    if msg:
        print (msg)
    sys.exit(0)

if __name__ == "__main__":
    try:
        # read the options and arguments
        opts, args = getopt.getopt(sys.argv[1:], "r")
        numArgs = len(args)
        print(opts, args)
        # assign defaults
        maxp = 2
        reverse = False
        
        # process the options and arguments
        for opt, val in opts:
          if opt == "-r":
             reverse = True
        if numArgs == 1:
            jobfile = args[0]
        elif numArgs == 2:
            jobfile, maxp = args
            try:
                maxp = int(maxp)
            except ValueError:
                exit("Error: enter an integer for maxp")
        else:
            exit()
        # RunJobs(jobfile, maxp, reverse)
    except getopt.GetoptError as e:
        exit("Error: %s" % e)