class AbstractCommand(object):

    """
    Utility class to run any bash command
    get the output, status, and error
    Example:
    cmd = Command("ls -la").run_command()
     cmd.command = ls -la
     cmd.returncode =  0
     com.error (a string containing the command's output to sderr) = ''
     com.output (a string containing the command's output to stdout)
    """

    def __init__(self, command):
        self.command = command

    def run_command(self, shell=True):
        import subprocess as sp
        process = sp.Popen(self.command, shell = shell, stdout = sp.PIPE, stderr = sp.PIPE)
        self.pid = process.pid
        self.output, self.error = process.communicate()
        self.failed = process.returncode
        return self

    @property
    def returncode(self):
        return self.failed
